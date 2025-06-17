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
    """Test __repr__() method."""
    # Repr vector
    assert matrix1.__repr__() == "Matrix2x2([\n  [1, 2],\n  [3, 4]\n])"


def test_add():
    """Test add() method."""
    # Add zeros
    assert matrix1.add(matrix0).matrix == matrix1.matrix

    # Add ints
    assert matrix1.add(matrix2).matrix == Matrix2x2(5, 5, 5, 5).matrix

    # Add wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        matrix1.add(-4)


def test_prod_r():
    """Test prod_r() method."""
    # Multiply by zero
    assert matrix1.prod_r(0).matrix == matrix0.matrix
    # Multiply by non-zero scalar
    assert matrix1.prod_r(2).matrix == Matrix2x2(2, 4, 6, 8).matrix


def test_prod():
    """Test prod() method."""
    # Multiply by matrix
    assert matrix1.prod(matrix2).matrix == Matrix2x2(8, 5, 20, 13).matrix
    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        matrix1.prod(Vector2(2, 3))


def test_determinant():
    """Test determinant() method."""
    assert abs(Matrix2x2(1, 2, 2, 3).determinant() - (-1.0)) < 1e-9


def test_solve_system():
    """Test solve_system() method."""
    matrix = Matrix2x2(2, 2, 3, -8)
    vector = Vector2(4, -1)

    # Test normal case (solve system from first math problem in lab 1)
    assert matrix.solve_system(vector) == Vector2(float(15/11), float(7/11))

    # Test wrong type input
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        matrix.solve_system(4)

    # Test non-invertible matrix (determinant == 0)
    singular_matrix = Matrix2x2(1, 2, 2, 4)  # det = 1*4 - 2*2 = 0
    with pytest.raises(ValueError, match="Matrix is not invertible"):
        singular_matrix.solve_system(Vector2(1, 2))
