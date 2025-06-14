"""Tests for verifying proper Vector functionality."""

import pytest
from Mathy import (Vector3,
                   HomogeneousVector3,
                   Matrix3x3,
                   Vector4,
                   HomothetyMatrix3x3,
                   TranslationMatrix3x3)


def test_constructor():
    """Test arguments' types for Vector3 constructor."""
    # Ints
    Vector3(1, 2, 3)

    # Floats
    Vector3(1.0, 2.0, 3.0)

    # Floats and ints
    Vector3(1, 2.0, 3)

    # Invalid types
    with pytest.raises(TypeError, match=r".* must be floats or ints.*"):
        Vector3(False, "a", [])


def test_norm():
    """Test norm() method."""
    # Norm zero
    assert abs(Vector3(0, 0, 0).norm) < 1e-9

    # Norm positive coordinates
    assert abs(Vector3(2, 4, 4).norm - 6.0) < 1e-9

    # Norm negative coordinates
    assert abs(Vector3(-2, -4, 4).norm - 6.0) < 1e-9


def test_eq():
    """Test __eq__() method."""
    # Compare different vectors
    assert Vector3(1, 1, 1) != Vector3(1, 1, -1)
    # Compare same vectors
    assert Vector3(1, 1, 1) == Vector3(1, 1, 1)
    # Compare a vector with a different type
    with pytest.raises(TypeError, match=r".* is not a Vector3.*"):
        Vector3(1, 2, 3) != 5


def test_repr():
    """Test __repr__() method."""
    # Repr vector
    assert Vector3(1, 3, 4).__repr__() == "Vector3(1, 3, 4)"


def test_add():
    """Test add() method."""
    # Add zeros
    assert Vector3(0, 0, 0).add(Vector3(0, 0, 0)) == Vector3(0, 0, 0)

    # Add ints
    assert Vector3(1, 2, 1).add(Vector3(3, -4, 2)) == Vector3(4, -2, 3)

    # Add floats
    assert Vector3(0.5, -1.0, 1.0).add(Vector3(3.5, 5.0, 1.0)) == Vector3(4.0, 4.0, 2.0)  # noqa: E501

    # Add wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector3.*"):
        Vector3(1, 2, 3).add(-4)


def test_subtract():
    """Test subtract() method."""
    # Subtract zeros
    assert Vector3(0, 0, 0).subtract(Vector3(0, 0, 0)) == Vector3(0, 0, 0)

    # Subtract ints
    assert Vector3(1, 2, 3).subtract(Vector3(1, 2, 3)) == Vector3(0, 0, 0)

    # Subtract floats
    assert Vector3(0.5, -1.0, 1.0).subtract(Vector3(3.5, 5.0, 1.0)) == Vector3(-3.0, -6.0, 0.0)  # noqa: E501

    # Subtract wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector3.*"):
        Vector3(1, 2, 3).subtract(-4)


def test_scalar_product():
    """Test scalar_product() method."""
    # Check scalar product values
    assert abs(Vector3(1, 1, 2).scalar_product(Vector3(1, -1, 2)) - 4) < 1e-9
    # Use wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector3.*"):
        Vector3(1, 1, 1).scalar_product(0)

    # Additional tests
    v1 = Vector3(1, -1, 2)
    v2 = Vector3(1, 2, 3)
    v3 = Vector3(4, 5, 6)

    assert abs((v1.scalar_product(v2) - 5)) < 1e-9
    assert abs((v3.scalar_product(v2) - 32)) < 1e-9
    assert abs((v3.scalar_product(v1) - 11)) < 1e-9

    # Check orthogonal vectors
    v5 = Vector3(1, 0, 0)
    v6 = Vector3(0, 1, 0)

    assert abs((v5.scalar_product(v6))) < 1e-9


def test_multiply_by_scalar():
    """Test multiply_by_scalar() method."""
    # Multiply by 0
    assert Vector3(1, 1, 1).multiply_by_scalar(0) == Vector3(0, 0, 0)
    # Multiply by int
    assert Vector3(1, 1, 1).multiply_by_scalar(2) == Vector3(2, 2, 2)
    # Multiply by float
    assert Vector3(1, 1, 1).multiply_by_scalar(0.5) == Vector3(0.5, 0.5, 0.5)
    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a float or int.*"):
        Vector3(1, 1, 1).multiply_by_scalar("z")


def test_multiply_by_matrix():
    """Test multiply_by_matrix() method."""
    # Multiply by matrix
    vec = Vector3(0, 0, 1)
    mat = Matrix3x3(1, 0, 1, 0, 1, 2, 0, 0, 1)
    assert vec.multiply_by_matrix(mat) == Vector3(1, 2, 1)

    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix3x3.*"):
        Vector3(0, 0, 1).multiply_by_matrix(Vector3(1, 1, 1))

    # Additional tests
    mat1 = HomothetyMatrix3x3(2)
    mat2 = HomothetyMatrix3x3(0)
    mat3 = TranslationMatrix3x3(1, 2)

    # Test 1
    v1 = Vector3(0, 3, 1)

    assert v1.multiply_by_matrix(mat1) == Vector3(0, 6, 1)
    assert v1.multiply_by_matrix(mat2) == Vector3(0, 0, 1)
    assert v1.multiply_by_matrix(mat3) == Vector3(1, 5, 1)

    # Test 2
    v2 = Vector3(1, 2, 3)

    assert v2.multiply_by_matrix(mat1) == Vector3(2, 4, 3)
    assert v2.multiply_by_matrix(mat2) == Vector3(0, 0, 3)
    assert v2.multiply_by_matrix(mat3) == Vector3(4, 8, 3)


def test_normalize():
    """Test normalize() method."""
    # Normalize vector
    assert Vector3(2, 4, 4).normalize() == Vector3(1/3, 2/3, 2/3)
    # Norm == 0
    with pytest.raises(ValueError, match=r"Cannot normalize a zero vector.*"):
        Vector3(0, 0, 0).normalize()


def test_cross_product():
    """Test cross_product() method."""
    # Canonical basis
    v1 = Vector3(1, 0, 0)
    v2 = Vector3(0, 1, 0)
    assert v1.cross_product(v2) == Vector3(0, 0, 1)

    # Random vectors
    v3 = Vector3(3, -5, 8)
    v4 = Vector3(12, 7, 2)
    assert v3.cross_product(v4) == Vector3(-66, 90, 81)

    # Wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector3.*"):
        Vector3(1, 1, 1).cross_product(0)


def test_homogenize():
    """Test homogenize() method."""
    from Mathy import Vector3
    assert Vector3(3, -4, 5).homogenize() == Vector4(3, -4, 5, 1)


def test_homogeneous_vector3():
    """Test HomogeneousVector3 class."""
    assert HomogeneousVector3(1, 2) == Vector3(1, 2, 1)
