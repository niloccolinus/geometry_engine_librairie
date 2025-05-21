"""Defines a 3D vector class."""


class Vector3:
    """A class to represent a 3D vector."""

    def __init__(self, x: float | int, y: float | int, z: float | int):
        """Initialize a 3D vector with the given x and y components."""
        self.x = x
        self.y = y
        self.z = z

    @property
    def norm(self) -> float:
        """Calculate the norm of the vector (accessible as a property)."""
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __eq__(self, other: 'Vector3') -> bool:
        """Check if two vectors are equal."""
        if isinstance(other, Vector3):
            return ((self.x == other.x) and (self.y == other.y)
                    and (self.z == other.z))
        else:
            raise TypeError(f"{other} is not a Vector3")

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def add(self, other: 'Vector3') -> 'Vector3':
        """Add two vectors together and return a new Vector3."""
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y,
                           self.z + other.z)
        else:
            raise TypeError(f"{other} is not a Vector3")

    def subtract(self, other: 'Vector3') -> 'Vector3':
        """
        Subtract another vector from the current vector.

        Return the result as a new Vector3.
        """
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y,
                           self.z - other.z)
        else:
            raise TypeError(f"{other} is not a Vector3")

    def scalar_product(self, other: 'Vector3') -> float:
        """Calculate the scalar (dot) product of two vectors."""
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f"{other} is not a Vector3")

    def multiply_by_scalar(self, factor: float | int) -> 'Vector3':
        """Multiply the vector by a scalar and return the resulting Vector3."""
        return Vector3(self.x * factor, self.y * factor, self.z * factor)

    def multiply_by_matrix(self, matrix) -> 'Vector3':
        """
        Multiply the vector by a 3x3 matrix.

        Return the resulting Vector3.
        """
        from Mathy import Matrix3x3
        if isinstance(matrix, Matrix3x3):
            a = matrix.matrix
            new_x = a[0][0] * self.x + a[0][1] * self.y + a[0][2] * self.z
            new_y = a[1][0] * self.x + a[1][1] * self.y + a[1][2] * self.z
            new_z = a[2][0] * self.x + a[2][1] * self.y + a[2][2] * self.z
            return Vector3(new_x, new_y, new_z)
        else:
            raise TypeError(f"{matrix} is not a Matrix3x3")

    def normalize(self) -> 'Vector3':
        """
        Normalize the vector.

        The new vector has the same direction and a length of 1.
        """
        n = self.norm
        if n == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector3(self.x / n, self.y / n, self.z / n)

    def cross_product(self, other: 'Vector3'):
        """Generate the cross product of 2 3D vectors."""
        if isinstance(other, Vector3):
            return Vector3(self.y * other.w - self.w * other.y,
                           self.w * other.x - self.x * other.w,
                           self.x * other.y - self.y * other.x)
        else:
            raise TypeError(f"{other} is not a Vector3")

    def homogenize(self):
        """Convert the vector to a 4D homogeneous vector."""
        from Mathy import HomogeneousVector4
        return HomogeneousVector4(self.x, self.y, self.z)


class HomogeneousVector3(Vector3):
    """
    A class to represent a vector in homogeneous coordinates.

    The projective space considered here is the projective plane.
    """

    def __init__(self, x, y):
        """Initialize a Vector3 in homogeneous coordinates."""
        super().__init__(x, y, 1)
        self.x = x
        self.y = y
