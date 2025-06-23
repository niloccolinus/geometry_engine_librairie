"""Tests for verifying proper Vector functionality."""

import pytest
from Mathy import Vector2
from Mathy import Matrix2x2


def test_norm():
    """Test norm() method."""
    # Norm zero
    assert abs(Vector2(0, 0).norm) < 1e-9

    # Norm positive coordinates
    assert abs(round(Vector2(2, 4).norm, 2) - 4.47) < 1e-9

    # Norm negative coordinates
    assert abs(round(Vector2(-2, -4).norm, 2) - 4.47) < 1e-9


def test_eq():
    """Test __eq__() method."""
    # Compare different vectors
    assert Vector2(1, 1) != Vector2(1, -1)
    # Compare same vectors
    assert Vector2(1, 1) == Vector2(1, 1)
    # Compare a vector with a different type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2) != 5


def test_repr():
    """Test __repr__() method."""
    # Repr vector
    assert Vector2(1, 3).__repr__() == "Vector2(1, 3)"


def test_add():
    """Test add() method."""
    # Add zeros
    assert Vector2(0, 0).add(Vector2(0, 0)) == Vector2(0, 0)

    # Add ints
    assert Vector2(1, 2).add(Vector2(3, -4)) == Vector2(4, -2)

    # Add floats
    assert Vector2(0.5, -1.0).add(Vector2(3.5, 5.0)) == Vector2(4.0, 4.0)

    # Add wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2).add(-4)


def test_subtract():
    """Test subtract() method."""
    # Subtract zeros
    assert Vector2(0, 0).subtract(Vector2(0, 0)) == Vector2(0, 0)

    # Subtract ints
    assert Vector2(1, 2).subtract(Vector2(3, -4)) == Vector2(-2, 6)

    # Subtract floats
    assert Vector2(0.5, -1.0).subtract(Vector2(3.5, 5.0)) == Vector2(-3.0, -6.0)  # noqa: E501

    # Subtract wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 2).subtract(-4)


def test_scalar_product():
    """Test scalar_product() method."""
    # Scalar product of v1 = [1, 1] and v2 = [1, -1]
    assert Vector2(1, 1).scalar_product(Vector2(1, -1)) == 0
    # Use wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector2.*"):
        Vector2(1, 1).scalar_product(0)


def test_multiply_by_scalar():
    """Test multiply_by_scalar() method."""
    # Multiply by 0
    assert Vector2(1, 1).multiply_by_scalar(0) == Vector2(0, 0)
    # Multiply by int
    assert Vector2(1, 1).multiply_by_scalar(2) == Vector2(2, 2)
    # Multiply by float
    assert Vector2(1, 1).multiply_by_scalar(0.5) == Vector2(0.5, 0.5)


def test_multiply_by_matrix():
    """Test multiply_by_matrix() method."""
    # Multiply by matrix
    assert Vector2(3, -4).multiply_by_matrix(Matrix2x2(2, 3, 4, -1)) == Vector2(-6, 16)  # noqa: E501
    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix2x2.*"):
        Vector2(3, -4).multiply_by_matrix(Vector2(2, 3))


def test_change_basis():
    """Test change_basis() method."""
    # Change basis
    assert Vector2(2, 3).change_basis(Vector2(1, 1), Vector2(1, -1)) == Vector2(2.5, -0.5)  # noqa: E501


def test_normalize():
    """Test normalize() method."""
    # Normalize vector
    assert Vector2(1, 0).normalize() == Vector2(1.0, 0.0)
    # Norm == 0
    with pytest.raises(ValueError, match=r"Cannot normalize a zero vector.*"):
        Vector2(0, 0).normalize()


def test_homogenize():
    """Test homogenize() method."""
    from Mathy import Vector3
    assert Vector2(3, -4).homogenize() == Vector3(3, -4, 1)
