"""Defines a 2x2 matrix class."""


class Matrix2x2:
    """A class to represent a 2 by 2 matrix."""

    def __init__(self, x1: float | int, x2: float | int,
                 x3: float | int, x4: float | int):
        """Initialize a 2x2 matrix with the given values."""
        self.matrix = [[x1, x2], [x3, x4]]

    def __repr__(self):
        """Return a string representation of the matrix."""
        return f"Matrix2x2([\n  {self.matrix[0]},\n  {self.matrix[1]}\n])"

    def add(self, matrix2: 'Matrix2x2') -> 'Matrix2x2':
        """Add two 2x2 matrices."""
        if isinstance(matrix2, Matrix2x2):
            res = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    res[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
            # Return a new Matrix2x2 object with the result of the addition
            return Matrix2x2(res[0][0], res[0][1], res[1][0], res[1][1])
        else:
            raise TypeError(f'{matrix2} is not a Matrix2x2')

    def prod_r(self, scalar: float | int) -> 'Matrix2x2':
        """Multiply the matrix by a scalar value."""
        if not isinstance(scalar, (int, float)):
            raise TypeError(f'{scalar} is not a scalar')
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                res[i][j] = self.matrix[i][j] * scalar
        # Return a new Matrix2x2 object
        # with the result of the scalar multiplication
        return Matrix2x2(res[0][0], res[0][1], res[1][0], res[1][1])

    def prod(self, matrix2: 'Matrix2x2') -> 'Matrix2x2':
        """Multiply two 2x2 matrices."""
        if isinstance(matrix2, Matrix2x2):
            a = self.matrix
            b = matrix2.matrix
            # Apply dot product for each element
            x1 = a[0][0] * b[0][0] + a[0][1] * b[1][0]
            x2 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
            x3 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
            x4 = a[1][0] * b[0][1] + a[1][1] * b[1][1]
            # Return a new Matrix2x2 object
            # with the result of the matrix multiplication
            return Matrix2x2(x1, x2, x3, x4)
        else:
            raise TypeError(f"{matrix2} is not a Matrix2x2")

    def determinant(self) -> float:
        """Calculate the determinant of a 2x2 matrix."""
        a = self.matrix[0][0]
        b = self.matrix[0][1]
        c = self.matrix[1][0]
        d = self.matrix[1][1]
        # The determinant of a 2x2 matrix is calculated as (ad - bc)
        return a * d - b * c

    def solve_system(self, b):
        """
        Solve a system of linear equations Ax = b.

        A is a matrix and b is a vector.
        """
        from Mathy import Vector2
        if isinstance(b, Vector2):
            det = self.determinant()
            a = self.matrix
            # Check if matrix is invertible
            if abs(det) < 1e-9:
                raise ValueError("Matrix is not invertible (determinant is zero). Cannot solve system.")  # noqa: E501
            # Calculate the determinant of the system for the x coordinate
            det_x = b.x * a[1][1] - b.y * a[0][1]
            # Calculate the determinant of the system for the y coordinate
            det_y = a[0][0] * b.y - a[1][0] * b.x
            # Use Cramer's rule to find the solutions for x and y
            x = det_x / det
            y = det_y / det
            # Return a new Vector2 object with the solutions for x and y
            return Vector2(x, y)
        else:
            raise TypeError(f"{b} is not a Vector2")
