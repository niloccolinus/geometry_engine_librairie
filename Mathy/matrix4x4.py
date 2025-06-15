"""Defines a 4x4 matrix class."""


from Mathy import cos, sin, deg, Matrix3x3

class Matrix4x4:
    """A class to represent a 4 by 4 matrix."""

    def __init__(
            self,
            x1: float | int, x2: float | int,
            x3: float | int, x4: float | int,
            x5: float | int, x6: float | int,
            x7: float | int, x8: float | int,
            x9: float | int, x10: float | int,
            x11: float | int, x12: float | int,
            x13: float | int, x14: float | int,
            x15: float | int, x16: float | int
            ):
        """Initialize a 4x4 matrix with the given values."""
        self.matrix = [
            [x1, x2, x3, x4], [x5, x6, x7, x8],
            [x9, x10, x11, x12], [x13, x14, x15, x16]]

    def __repr__(self):
        """Return a string representation of the matrix."""
        return f"Matrix4x4([\n {self.matrix[0]},\n {self.matrix[1]},\n {self.matrix[2]},\n {self.matrix[3]}\n])"  # noqa: E501

    def __eq__(self, other: 'Matrix4x4') -> bool:
        """Check if two 4x4 matrices are equal."""
        if isinstance(other, Matrix4x4):
            for i in range(4):
                for j in range(4):
                    if abs(self.matrix[i][j] - other.matrix[i][j]) >= 1e-9:
                        return False
            return True
        else:
            raise TypeError(f"{other} is not a Matrix4x4")

    def add(self, other: 'Matrix4x4') -> 'Matrix4x4':
        """Add two 4x4 matrices."""
        if isinstance(other, Matrix4x4):
            res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for i in range(4):
                for j in range(4):
                    res[i][j] = self.matrix[i][j] + other.matrix[i][j]
            # Return a new Matrix4x4 object with the result of the addition
            return Matrix4x4(
                res[0][0], res[0][1], res[0][2], res[0][3],
                res[1][0], res[1][1], res[1][2], res[1][3],
                res[2][0], res[2][1], res[2][2], res[2][3],
                res[3][0], res[3][1], res[3][2], res[3][3],
            )
        else:
            raise TypeError(f'{other} is not a Matrix4x4')

    def prod_r(self, scalar: float | int) -> 'Matrix4x4':
        """Multiply the matrix by a scalar value."""
        if not isinstance(scalar, (int, float)):
            raise TypeError(f'{scalar} is not a scalar')
        res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                res[i][j] = self.matrix[i][j] * scalar
        # Return a new Matrix4x4 object
        # with the result of the scalar multiplication
        return Matrix4x4(
            res[0][0], res[0][1], res[0][2], res[0][3],
            res[1][0], res[1][1], res[1][2], res[1][3],
            res[2][0], res[2][1], res[2][2], res[2][3],
            res[3][0], res[3][1], res[3][2], res[3][3],
        )

    def prod(self, other: 'Matrix4x4') -> 'Matrix4x4':
        """Multiply two 4x4 matrices."""
        if isinstance(other, Matrix4x4):
            a = self.matrix
            b = other.matrix
            res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        res[i][j] += a[i][k] * b[k][j]
            # Return a new Matrix4x4 object
            # with the result of the matrix multiplication
            return Matrix4x4(
                res[0][0], res[0][1], res[0][2], res[0][3],
                res[1][0], res[1][1], res[1][2], res[1][3],
                res[2][0], res[2][1], res[2][2], res[2][3],
                res[3][0], res[3][1], res[3][2], res[3][3],
            )
        else:
            raise TypeError(f'{other} is not a Matrix4x4')

    def determinant(self) -> float:
        """Calculate the determinant of a 4x4 matrix."""
        a, b, c, d = self.matrix[0]
        e, f, g, h = self.matrix[1]
        i, j, k, l_ = self.matrix[2]
        m, n, o, p = self.matrix[3]
        # The determinant of a 4x4 matrix is calculated as
        # det = a * det(mat1) − b * det(mat2) + c * det(mat3) - d * det(mat4)
        # where mat1, mat2, mat3 and mat4 are 3x3 submatrices
        # 1) Extract the submatrices from our 4x4 matrix
        mat1 = Matrix3x3(f, g, h, j, k, l_, n, o, p)
        mat2 = Matrix3x3(e, g, h, i, k, l_, m, o, p)
        mat3 = Matrix3x3(e, f, h, i, j, l_, m, n, p)
        mat4 = Matrix3x3(e, f, g, i, j, k, m, n, o)
        # 2) Get the determinants of each submatrix
        det1 = mat1.determinant()
        det2 = mat2.determinant()
        det3 = mat3.determinant()
        det4 = mat4.determinant()
        # 3) Apply the formula
        return (a * det1 - b * det2 + c * det3 - d * det4)

    def round(self, decimal: int) -> 'Matrix4x4':
        """Return a rounded approximation of the matrix's contents."""
        if (decimal >= 0 and isinstance(decimal, int)):
            res = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for i in range(4):
                for j in range(4):
                    res[i][j] = round(self.matrix[i][j], decimal)
                    if res[i][j] == -0.0:
                        res[i][j] = abs(res[i][j])
            return Matrix4x4(
                res[0][0], res[0][1], res[0][2], res[0][3],
                res[1][0], res[1][1], res[1][2], res[1][3],
                res[2][0], res[2][1], res[2][2], res[2][3],
                res[3][0], res[3][1], res[3][2], res[3][3],
                )
        else:
            if (decimal < 0):
                raise ValueError(f'{decimal} should not be negative.')
            if not isinstance(decimal, int):
                raise TypeError(f'{decimal} should be an int.')


class TranslationMatrix4x4(Matrix4x4):
    """A class to represent a 4 by 4 translation matrix."""

    def __init__(self, a, b, c):
        """Initialize a translation matrix."""
        super().__init__(
            1, 0, 0, a,
            0, 1, 0, b,
            0, 0, 1, c,
            0, 0, 0, 1
        )
        self.a = a
        self.b = b
        self.c = c


class RotationMatrix4x4_x(Matrix4x4):
    """
    A class to represent a 4 by 4 rotation matrix.

    Parameters:
        theta (float): Angle of rotation in degrees.
    """

    def __init__(self, t_degrees):
        """Initialize a rotation matrix."""
        theta = deg(t_degrees)  # Convert degrees to radians
        super().__init__(
            1, 0, 0, 0,
            0, cos(theta), -sin(theta), 0,
            0, sin(theta), cos(theta), 0,
            0, 0, 0, 1
        )
        self.t_radians = theta


class RotationMatrix4x4_y(Matrix4x4):
    """
    A class to represent a 4 by 4 rotation matrix.

    Parameters:
        theta (float): Angle of rotation in degrees.
    """

    def __init__(self, t_degrees):
        """Initialize a rotation matrix."""
        theta = deg(t_degrees)  # Convert degrees to radians
        super().__init__(
            cos(theta), 0, sin(theta), 0,
            0, 1, 0, 0,
            -sin(theta), 0, cos(theta), 0,
            0, 0, 0, 1
        )
        self.t_radians = theta


class RotationMatrix4x4_z(Matrix4x4):
    """
    A class to represent a 4 by 4 rotation matrix.

    Parameters:
        theta (float): Angle of rotation in degrees.
    """

    def __init__(self, t_degrees):
        """Initialize a rotation matrix."""
        theta = deg(t_degrees)  # Convert degrees to radians
        super().__init__(
            cos(theta), -sin(theta), 0, 0,
            sin(theta), cos(theta), 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        )
        self.t_radians = theta


class HomothetyMatrix4x4(Matrix4x4):
    """A class to represent a 4 by 4 homothety matrix."""

    def __init__(self, k):
        """Initialize a homotethy matrix."""
        super().__init__(
            k, 0, 0, 0,
            0, k, 0, 0,
            0, 0, k, 0,
            0, 0, 0, 1
        )
        self.k = k


class AnisotropicMatrix4x4(Matrix4x4):
    """A class to represent an anisotropic scaling matrix."""

    def __init__(self, sx, sy, sz):
        """Initialize an anisotropic scaling matrix."""
        super().__init__(
            sx, 0, 0, 0,
            0, sy, 0, 0,
            0, 0, sz, 0,
            0, 0, 0, 1
        )
        self.sx = sx
        self.sy = sy
        self.sz = sz


class TotalRotationMatrix4x4(Matrix4x4):
    """A class to represent a rotation matrix combining x, y, and z axes."""

    def __init__(self,
                 rot_x: RotationMatrix4x4_x,
                 rot_y: RotationMatrix4x4_y,
                 rot_z: RotationMatrix4x4_z):
        """Initialize a multi-axis rotation matrix."""
        self.matrix = (rot_z.prod(rot_y)).prod(rot_x)
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.rot_z = rot_z
