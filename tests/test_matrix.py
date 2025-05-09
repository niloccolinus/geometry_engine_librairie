"""Tests for verifying proper Matrix functionality."""

import pytest
from Mathy import Vector2
from Mathy import Matrix2x2


# Example matrix 0
matrix0 = Matrix2x2(0, 0, 0, 0)

# Example matrix 1
matrix1 = Matrix2x2(1, 2, 3, 4)

# Example matrix 0
matrix2 = Matrix2x2(4, 3, 2, 1)


def test_repr():
    # Repr vector
    assert matrix1.__repr__() == "Matrix2x2([\n  [1, 2],\n  [3, 4]\n])"


def test_add():
    # Add zeros
    assert matrix1.add(matrix0).matrix == matrix1.matrix

    # Add ints
    assert matrix1.add(matrix2).matrix == Matrix2x2(5, 5, 5, 5).matrix

    # Add wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        matrix1.add(-4)


def test_prod_r():
    # Multiply by zero
    assert matrix1.prod_r(0).matrix == matrix0.matrix
    # Multiply by non-zero scalar
    assert matrix1.prod_r(2).matrix == Matrix2x2(2, 4, 6, 8).matrix


def test_prod():
    # Multiply by matrix
    assert matrix1.prod(matrix2).matrix == Matrix2x2(8, 5, 20, 13).matrix
    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        matrix1.prod(Vector2(2, 3))


def test_determinant():
    assert Matrix2x2(1, 2, 2, 3).determinant() == -1.0


def test_solve_system():
    # Solve system from first math problem in lab 1
    matrix = Matrix2x2(2, 2, 3, -8)
    vector = Vector2(4, -1)
    assert matrix.solve_system(vector) == Vector2(float(15/11), float(7/11))
    # Pass wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        matrix1.solve_system(4)
