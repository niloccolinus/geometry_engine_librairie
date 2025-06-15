"""Defines a GameObject class."""

from Mathy import Transform, Renderer3D, HomogeneousVector4


class GameObject:
    """Represents a 3D object in the scene with a transform and a renderer."""

    def __init__(self, name="GameObject", vertices=None, indices=None):
        """Initialize a game object."""
        self.name = name
        # 3D mesh data
        self.vertices = vertices or []
        self.indices = indices or []
        # Transform and renderer components
        self.transform = Transform()
        self.renderer = Renderer3D(self.vertices, self.indices)


class Cube(GameObject):
    """A class to represent a cube."""

    def __init__(self):
        """Initialize a cubic game object."""
        super().__init__("Cube",
                         [HomogeneousVector4(-1.0, -1.0,  1.0),
                          HomogeneousVector4(1.0, -1.0,  1.0),
                          HomogeneousVector4(-1.0,  1.0,  1.0),
                          HomogeneousVector4(1.0,  1.0,  1.0),
                          HomogeneousVector4(-1.0, -1.0, -1.0),
                          HomogeneousVector4(1.0, -1.0, -1.0),
                          HomogeneousVector4(-1.0,  1.0, -1.0),
                          HomogeneousVector4(1.0,  1.0, -1.0,)],
                         [0, 1, 2, 3, 7, 1, 5, 4, 7, 6, 2, 4, 0, 1])
