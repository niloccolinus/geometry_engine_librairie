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
        # Generate edges
        self.edges = []
        self.homogeneous_normals = []
        for t in range(0, len(self.indices) - 2, 1):
            i0 = self.indices[t]
            i1 = self.indices[t + 1]
            i2 = self.indices[t + 2]
            edge1 = self.vertices[i1].subtract(self.vertices[i0])
            edge2 = self.vertices[i2].subtract(self.vertices[i0])
            normal = edge1.cross_product(edge2)
            # normalized_normal = normal.normalize()
            self.edges.append((self.vertices[i0], self.vertices[i1]))
            self.edges.append((self.vertices[i1], self.vertices[i2]))
            # self.normals.append(normalized_normal)
            # self.homogeneous_normals.append(normalized_normal.homogenize())


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
                         Vector3(1.0,  1.0, -1.0)],
                         [
                     0, 1,  # front bottom edge (AB)
                     1, 3,  # front right edge (BD)
                     3, 2,  # front top edge (DC)
                     2, 0,  # front left edge (CA)
                     4, 5,  # back bottom edge (EF)
                     5, 7,  # back right edge (FH)
                     7, 6,  # back top edge (HG)
                     6, 4,  # back left edge (GE)
                     0, 4,  # left bottom edge (AE)
                     1, 5,  # right bottom edge (BF)
                     2, 6,  # left top edge (CG)
                     3, 7   # right top edge (DH)
                         ])


class Airplane(GameObject):
    """A class to represent an airplane using three cubic meshes."""

    def __init__(self, wing_scale: float):
        """Initialize an airplane-like game object."""
        # Make sure the wings are appropriately sized
        if (wing_scale > 0 and wing_scale <= 0.5) and isinstance(wing_scale, float):  # noqa: E501
            self.wing_scale = wing_scale
        elif not isinstance(wing_scale, float):
            raise TypeError("wing_scale must be a float!")
        else:
            raise ValueError("wing_scale must be greater than 0 and less than or equal to 0.5!")  # noqa: E501

        # Create a cube to represent the body of the airplane
        self.body = Cube()
        # Create wings that are proportional to the body of the airplane
        self.left_wing = Cube()
        self.left_wing.transform.homothetic_scale(self.wing_scale)
        self.right_wing = Cube()
        self.right_wing.transform.homothetic_scale(self.wing_scale)

        # Calculate the length of an edge for the body of the airplane
        self.body_edge = (self.body.vertices[0].subtract(self.body.vertices[1])).norm  # noqa: E501

        # Locate the wings adjacent to the body of the airplane
        self.wing_offset = self.body_edge / 2 + self.body_edge * wing_scale / 2
        self.left_wing.transform.translate(0, 0, -self.wing_offset)
        self.right_wing.transform.translate(0, 0, self.wing_offset)
