"""Defines a 3D renderer class."""

from Mathy import GameObject


class Renderer3D(object):
    """A class to contain render data."""

    def convert_local_to_world(self, game_object: GameObject):
        """Apply world coordinates to game object."""
        model_matrix = game_object.transform.transform_matrix
        world_vertices = []
        for vertex in game_object.homogeneous_vertices:
            world_vertices.append(vertex.multiply_by_matrix(model_matrix))
        return world_vertices
