"""Defines a GameObject class."""

from Mathy import Transform, Renderer3D, Vector3


class GameObject:
    """Represents a 3D object in the scene with a transform and a renderer."""

    def __init__(self, vertices: list[Vector3],
                 indices: list[int], name="GameObject"):
        """Initialize a game object."""
        self.name = name
        # 3D mesh data
        self.vertices = vertices
        self.indices = indices
        # Transform and renderer components
        self.transform = Transform()
        self.renderer = Renderer3D()
        # Generate vertices in homogeneous coordinates
        self.homogeneous_vertices = []
        for vertex in self.vertices:
            self.homogeneous_vertices.append(vertex.homogenize())
        # Generate normals
        self.normals = []
        self.homogeneous_normals = []
        # Iterate over triangles (groups of 3 indices)
        for t in range(0, len(self.indices) - 2, 3):
            i0 = self.indices[t]
            i1 = self.indices[t + 1]
            i2 = self.indices[t + 2]
            edge1 = self.vertices[i1].subtract(self.vertices[i0])
            edge2 = self.vertices[i2].subtract(self.vertices[i0])
            normal = edge1.cross_product(edge2)
            normalized_normal = normal.normalize()
            self.normals.append(normalized_normal)
            self.homogeneous_normals.append(normalized_normal.homogenize())


class Cube(GameObject):
    """A class to represent a cube."""

    def __init__(self):
        """Initialize a cubic game object."""
        super().__init__([Vector3(-1.0, -1.0,  1.0),
                          Vector3(1.0, -1.0,  1.0),
                          Vector3(-1.0,  1.0,  1.0),
                          Vector3(1.0,  1.0,  1.0),
                          Vector3(-1.0, -1.0, -1.0),
                          Vector3(1.0, -1.0, -1.0),
                          Vector3(-1.0,  1.0, -1.0),
                          Vector3(1.0,  1.0, -1.0,)],
                         [0, 1, 2, 3, 7, 1, 5, 4, 7, 6, 2, 4, 0, 1])
