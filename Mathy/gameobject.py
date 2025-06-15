"""Defines a GameObject class."""

from Mathy import Transform, Renderer3D, Vector3


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
        # Generate vertices in homogeneous coordinates
        self.homogeneous_vertices = []
        for vertex in self.vertices:
            self.homogeneous_vertices.append(vertex.homogenize())
        # Generate normals
        self.normals = []
        self.homogeneous_normals = []
        for i in self.indices[:-2]:
            edge1 = self.vertices[i] - self.vertices[i + 1]
            edge2 = self.vertices[i] - self.vertices[i + 2]
            normal = edge1.cross_product(edge2)
            normalized_normal = normal.normalize()
            self.normals.append[normalized_normal]
            self.homogeneous_normals.append[normalized_normal.homogenize()]


class Cube(GameObject):
    """A class to represent a cube."""

    def __init__(self):
        """Initialize a cubic game object."""
        super().__init__("Cube",
                         [Vector3(-1.0, -1.0,  1.0),
                          Vector3(1.0, -1.0,  1.0),
                          Vector3(-1.0,  1.0,  1.0),
                          Vector3(1.0,  1.0,  1.0),
                          Vector3(-1.0, -1.0, -1.0),
                          Vector3(1.0, -1.0, -1.0),
                          Vector3(-1.0,  1.0, -1.0),
                          Vector3(1.0,  1.0, -1.0,)],
                         [0, 1, 2, 3, 7, 1, 5, 4, 7, 6, 2, 4, 0, 1])
