"""Defines a 3D renderer class."""

from Mathy import HomogeneousVector4, Triangle3D, Vector3


class Renderer3D(object):
    """A class to contain render data."""

    def convert_local_to_world(self, game_object):
        """Apply world coordinates to game object."""
        model_matrix = game_object.transform.transform_matrix
        world_vertices = []
        triangles_world = []
        for vertex in game_object.homogeneous_vertices:
            world_vertices.append(vertex.multiply_by_matrix(model_matrix))
        for triangle in game_object.triangles:
            pa = triangle.pa.multiply_by_matrix(model_matrix)
            pb = triangle.pb.multiply_by_matrix(model_matrix)
            pc = triangle.pc.multiply_by_matrix(model_matrix)
            triangles_world.append(Triangle3D(pa, pb, pc, triangle.indices))
        return (world_vertices, triangles_world)
    
    def set_mesh_data(self, gameobject):
        """Set mesh data for rendering."""
        self.vertices = gameobject.homogeneous_vertices
        self.indices = gameobject.indices
        self.triangles = []
        for i in range(0, len(self.indices) - 1, 3):
            p1 = Vector3(self.vertices[self.indices[i]].x,
                 self.vertices[self.indices[i]].y,
                 self.vertices[self.indices[i]].z).homogenize()
            p2 = Vector3(self.vertices[self.indices[i + 1]].x,
                 self.vertices[self.indices[i + 1]].y,
                 self.vertices[self.indices[i + 1]].z).homogenize()
            p3 = Vector3(self.vertices[self.indices[i + 2]].x,
                 self.vertices[self.indices[i + 2]].y,
                 self.vertices[self.indices[i + 2]].z).homogenize()
            self.triangles.append(Triangle3D(p1, p2, p3, {
                "pa": self.indices[i],
                "pb": self.indices[i + 1],
                "pc": self.indices[i + 2]
            }))
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
