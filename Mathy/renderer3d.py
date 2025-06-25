"""Defines a 3D renderer class."""

from Mathy import (HomogeneousVector4,
                   Triangle3D,
                   Vector3,
                   barycentric_coordinates)


class Renderer3D(object):
    """A class to contain render data."""

    def __init__(self, screen_width=800, screen_height=600):
        """Initialize the renderer."""
        self.vertices = []
        self.indices = []
        self.triangles = []
        self.z_buffer = []
        self.framebuffer_color = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.texture = None  # Placeholder for texture data

    def clear(self):
        """Clear the renderer data."""
        self.vertices = []
        self.indices = []
        self.triangles = []
        self.clear_z_buffer()

    def clear_z_buffer(self):
        # Initialize z-buffer and framebuffer for our screen size
        self.z_buffer = []
        self.framebuffer_color = []
        for _ in range(self.screen_width):
            self.z_buffer.append([float('inf')] * self.screen_height)
            self.framebuffer_color.append([(0, 0, 0)] * self.screen_height)

    def convert_local_to_world(self, game_object):
        """Apply world coordinates to game object."""
        model_matrix = game_object.transform.transform_matrix
        triangles_world = []
        for triangle in game_object.triangles:
            pa = triangle.pa.multiply_by_matrix(model_matrix)
            pb = triangle.pb.multiply_by_matrix(model_matrix)
            pc = triangle.pc.multiply_by_matrix(model_matrix)
            triangles_world.append(Triangle3D(pa, pb, pc, triangle.indices,
                                              triangle.uv))
        return triangles_world

    def set_mesh_data(self, gameobject):
        """Set mesh data for rendering."""
        self.vertices = gameobject.homogeneous_vertices
        self.indices = gameobject.indices
        self.triangles = []
        self.texture = gameobject.texture
        for i in range(0, len(self.indices) - 1, 3):
            p1 = Vector3(self.vertices[self.indices[i]].x,
                         self.vertices[self.indices[i]].y,
                         self.vertices[self.indices[i]].z).homogenize()
            p1_uv = gameobject.uv[self.indices[i]] if gameobject.uv else (0, 0)
            p2 = Vector3(self.vertices[self.indices[i + 1]].x,
                         self.vertices[self.indices[i + 1]].y,
                         self.vertices[self.indices[i + 1]].z).homogenize()
            p2_uv = gameobject.uv[self.indices[i + 1]
                                  ] if gameobject.uv else (0, 0)
            p3 = Vector3(self.vertices[self.indices[i + 2]].x,
                         self.vertices[self.indices[i + 2]].y,
                         self.vertices[self.indices[i + 2]].z).homogenize()
            p3_uv = gameobject.uv[self.indices[i + 2]
                                  ] if gameobject.uv else (0, 0)
            self.triangles.append(Triangle3D(p1, p2, p3, {
                "pa": self.indices[i],
                "pb": self.indices[i + 1],
                "pc": self.indices[i + 2]
            }, (p1_uv, p2_uv, p3_uv)))
        gameobject.triangles = self.triangles

    def project_vertices(self, vertices, camera, projection):
        """Project vertices from 3D space to 2D screen space."""
        projected_vertices = []
        for vertex in vertices:
            vertex: HomogeneousVector4 = vertex
            # Apply view transformation
            view_vertex: HomogeneousVector4 = vertex.multiply_by_matrix(camera.get_view_matrix())  # noqa: E501
            # Apply projection transformation
            projected_vertex: HomogeneousVector4 = view_vertex.multiply_by_matrix(projection.get_projection_matrix())  # noqa: E501
            # Convert to screen coordinates
            screen_vertex = projection.get_screen_coordinates(projected_vertex)
            projected_vertices.append(screen_vertex)
        return projected_vertices

    def project_triangle(self, triangle, camera, projection):
        """Project a triangle from 3D space to 2D screen space."""
        p1 = self.project_vertices([triangle.pa], camera, projection)[0]
        p2 = self.project_vertices([triangle.pb], camera, projection)[0]
        p3 = self.project_vertices([triangle.pc], camera, projection)[0]
        return (p1, p2, p3)

    def draw_2d_triangle(self, triangle,  camera, projection, renderer,
                         rasterize=True):
        """Draw a triangle in 2D space."""
        p1, p2, p3 = self.project_triangle(triangle, camera, projection)
        projected_triangle = Triangle3D(
            Vector3(p1.x, p1.y, p1.z),
            Vector3(p2.x, p2.y, p2.z),
            Vector3(p3.x, p3.y, p3.z),
            triangle.indices,
            triangle.uv
        )
        if rasterize is False:
            renderer.draw_triangle(
                (p1.x, p1.y),
                (p2.x, p2.y),
                (p3.x, p3.y),
                color=(0.5, 0.5, 0.5)
            )
        else:
            pixels = self.rasterize_triangle(projected_triangle)
            for x, y, color in pixels:
                renderer.draw_point(x, y, color, radius=1)

    def is_in_front_of_camera(self, z_pixel, x, y):
        """Check if the pixel is in front of the camera."""
        return z_pixel < self.z_buffer[x][y]

    def interpolate_texture_coordinates(self, lambda_A, lambda_B, lambda_C,
                                        uv1, uv2, uv3):
        """Interpolate texture coordinates based on barycentric coordinates."""
        u = lambda_A * uv1[0] + lambda_B * uv2[0] + lambda_C * uv3[0]
        v = lambda_A * uv1[1] + lambda_B * uv2[1] + lambda_C * uv3[1]
        return (u, v)

    def interpolate_color(self, lambda_A, lambda_B, lambda_C):
        """Compute the color using barycentric coordinates."""
        c_p1 = (100, 200, 100)  # Color for vertex A
        c_p2 = (200, 100, 100)  # Color for vertex B
        c_p3 = (100, 100, 200)  # Color for vertex C
        color_pixel = (
            c_p1[0] * lambda_A + c_p2[0] * lambda_B + c_p3[0] * lambda_C,
            c_p1[1] * lambda_A + c_p2[1] * lambda_B + c_p3[1] * lambda_C,
            c_p1[2] * lambda_A + c_p2[2] * lambda_B + c_p3[2] * lambda_C
        )
        return color_pixel

    def rasterize_triangle(self, triangle):
        """Compute triangle rasterization."""
        # bounding box
        p1, p2, p3 = triangle.get_vertices()
        xmin = min(p1.x, p2.x, p3.x)
        xmax = max(p1.x, p2.x, p3.x)
        ymin = min(p1.y, p2.y, p3.y)
        ymax = max(p1.y, p2.y, p3.y)
        pixels = []
        # Cicle through each pixel in the bounding box
        for x in range(int(xmin), int(xmax) + 1):
            for y in range(int(ymin), int(ymax) + 1):
                # Compute the pixel's center
                center_x = x + 0.5
                center_y = y + 0.5
                # Determine if the pixel is inside the triangle
                # using barycentric coordinates
                p = Vector3(center_x, center_y, 0)
                lambda_A, lambda_B, lambda_C = barycentric_coordinates(
                    p, p1, p2, p3)
                if (
                    0 <= lambda_A <= 1 and
                    0 <= lambda_B <= 1 and
                    0 <= lambda_C <= 1 and
                    # Due to floating point precision issues,
                    # we allow a small tolerance
                    # for values extremely close to 1
                    abs(lambda_A + lambda_B + lambda_C - 1) < 1e-8
                ):
                    # The pixel is inside the triangle
                    # draw it based on its depth
                    z_pixel = lambda_A * p1.z + lambda_B * p2.z + lambda_C * p3.z  # noqa: E501
                    if self.is_in_front_of_camera(z_pixel, x, y):
                        self.z_buffer[x][y] = z_pixel
                        # u_pixel, v_pixel =
                        # self.interpolate_texture_coordinates(
                        #     lambda_A, lambda_B, lambda_C,
                        #     triangle.uv[0], triangle.uv[1], triangle.uv[2]
                        # )
                        color = self.interpolate_color(
                            lambda_A, lambda_B, lambda_C
                        )
                        self.framebuffer_color[x][y] = color
                        # # Clamp texture coordinates to [0, 1]
                        # u_pixel = max(0, min(1, u_pixel))
                        # v_pixel = max(0, min(1, v_pixel))
                        # # Compute the color based on texture coordinates
                        # x_tex = int(u_pixel * (150 - 1))
                        # y_tex = int(v_pixel * (150 - 1))
                        # tex_index = y_tex * 150 + x_tex
                        # self.framebuffer_color[x][y] = (
                        #     self.texture[tex_index]
                        # )
                    pixels.append((x, y, self.framebuffer_color[x][y]))
        return pixels
