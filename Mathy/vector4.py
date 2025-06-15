"""Defines vector class for spatial geometry."""


class Vector4:
    """A class to represent a 4-dimensional vector."""

    def __init__(self, x: float | int, y: float | int, z: float | int,
                 w: float | int):
        """Initialize a 4D vector with the given components."""
        if all(isinstance(i, (int, float)) for i in [x, y, z, w]):
            self.x = x
            self.y = y
            self.z = z
            self.w = w
        else:
            raise TypeError("All components must be floats or ints.")

    @property
    def norm(self) -> float:
        """Calculate the norm of the vector (accessible as a property)."""
        return (self.x**2 + self.y**2 + self.z**2 + self.w**2)**0.5

    def __eq__(self, other: 'Vector4') -> bool:
        """Check if two vectors are equal."""
        if isinstance(other, Vector4):
            return ((abs(self.x - other.x) < 1e-9)
                    and (abs(self.y - other.y) < 1e-9)
                    and (abs(self.z - other.z) < 1e-9)
                    and (abs(self.w - other.w) < 1e-9))
        else:
            raise TypeError(f"{other} is not a Vector4")

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector4({self.x}, {self.y}, {self.z}, {self.w})"

    def scalar_product(self, other: 'Vector4') -> float:
        """Calculate the scalar (dot) product of two vectors."""
        if isinstance(other, Vector4):
            return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w  # noqa: E501
        else:
            raise TypeError(f"{other} is not a Vector4")

    def multiply_by_scalar(self, factor: float | int) -> 'Vector4':
        """Multiply the vector by a scalar and return the resulting Vector4."""
        if isinstance(factor, (float, int)):
            return Vector4(self.x * factor, self.y * factor,
                           self.z * factor, self.w * factor)
        else:
            raise TypeError(f"{factor} is not a float or int.")

    def multiply_by_matrix(self, matrix) -> 'Vector4':
        """
        Multiply the vector by a 4x4 matrix.

        Return the resulting Vector4.
        """
        from Mathy import Matrix4x4
        if isinstance(matrix, Matrix4x4):
            a = matrix.matrix
            new_x = a[0][0] * self.x + a[0][1] * self.y + a[0][2] * self.z + a[0][3] * self.w  # noqa: E501
            new_y = a[1][0] * self.x + a[1][1] * self.y + a[1][2] * self.z + a[1][3] * self.w  # noqa: E501
            new_z = a[2][0] * self.x + a[2][1] * self.y + a[2][2] * self.z + a[2][3] * self.w  # noqa: E501
            new_w = a[3][0] * self.x + a[3][1] * self.y + a[3][2] * self.z + a[3][3] * self.w  # noqa: E501
            return Vector4(new_x, new_y, new_z, new_w)
        else:
            raise TypeError(f"{matrix} is not a Matrix4x4")

    def add(self, other: 'Vector4') -> 'Vector4':
        """Add two vectors together and return a new Vector4."""
        if isinstance(other, Vector4):
            return Vector4(self.x + other.x, self.y + other.y,
                           self.z + other.z, self.w + other.w)
        else:
            raise TypeError(f"{other} is not a Vector4")
    
    def subtract(self, other: 'Vector4') -> 'Vector4':
        """
        Subtract another vector from the current vector.

        Return the result as a new Vector4.
        """
        if isinstance(other, Vector4):
            return Vector4(self.x - other.x, self.y - other.y,
                           self.z - other.z, self.w - other.w)
        else:
            raise TypeError(f"{other} is not a Vector4")

    def normalize(self) -> 'Vector4':
        """
        Normalize the vector.

        The new vector has the same direction and a length of 1.
        """
        n = self.norm
        if abs(n) < 1e-9:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector4(self.x / n, self.y / n, self.z / n, self.w / n)


class HomogeneousVector4(Vector4):
    """
    A class to represent a vector in homogeneous coordinates.

    The projective space considered here is the projective plane.
    """

    def __init__(self, x, y, z):
        """Initialize a Vector4 in homogeneous coordinates."""
        super().__init__(x, y, z, 1)
        self.x = x
        self.y = y
        self.z = z
