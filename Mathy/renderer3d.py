"""Defines a 3D renderer class."""

from Mathy import HomogeneousVector4


class Renderer3D(object):
    """A class to contain render data."""

    def convert_local_to_world(self, game_object):
        """Apply world coordinates to game object."""
        model_matrix = game_object.transform.transform_matrix
        world_vertices = []
        for vertex in game_object.homogeneous_vertices:
            world_vertices.append(vertex.multiply_by_matrix(model_matrix))
        return world_vertices

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
