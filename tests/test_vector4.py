"""Tests for verifying proper Vector functionality."""

import pytest
from Mathy import (Vector4,
                   HomogeneousVector4,
                   HomothetyMatrix4x4,
                   TranslationMatrix4x4)


def test_constructor():
    """Test arguments' types for Vector4 constructor."""
    # Ints
    Vector4(1, 2, 3, 4)

    # Floats
    Vector4(1.0, 2.0, 3.0, 4.0)

    # Floats and ints
    Vector4(1, 2.0, 3, 4.0)

    # Invalid types
    with pytest.raises(TypeError, match=r".* must be floats or ints.*"):
        Vector4(0, "a", None, [])


def test_norm():
    """Test norm() method."""
    # Norm zero
    assert abs(Vector4(0, 0, 0, 0).norm) < 1e-9

    # Norm positive coordinates
    assert abs(Vector4(2, 4, 4, 0).norm - 6.0) < 1e-9

    # Norm negative coordinates
    assert abs(Vector4(-2, -4, 4, 0).norm - 6.0) < 1e-9


def test_eq():
    """Test __eq__() method."""
    # Compare different vectors
    assert Vector4(1, 1, 1, 1) != Vector4(1, 1, -1, -1)

    # Compare same vectors
    assert Vector4(1, 1, 1, 1) == Vector4(1, 1, 1, 1)

    # Compare a vector with a different type
    with pytest.raises(TypeError, match=r".* is not a Vector4.*"):
        Vector4(1, 2, 3, 4) != 5


def test_repr():
    """Test __repr__() method."""
    # Repr vector
    assert Vector4(1, 3, 4, 5).__repr__() == "Vector4(1, 3, 4, 5)"


def test_scalar_product():
    """Test scalar_product() method."""
    # Check scalar product values
    v1 = Vector4(1, 1, 2, 0)
    v2 = Vector4(1, -1, 2, 0)
    v3 = Vector4(1, 2, 3, 4)
    v4 = Vector4(5, 6, 7, 8)

    assert abs((v1.scalar_product(v2) - 4)) < 1e-9
    assert abs((v3.scalar_product(v4) - 70)) < 1e-9
    assert abs((v1.scalar_product(v4) - 25)) < 1e-9
    assert abs((v2.scalar_product(v3) - 5)) < 1e-9

    # Check orthogonal vectors
    v5 = Vector4(1, 0, 0, 0)
    v6 = Vector4(0, 1, 0, 0)

    assert abs((v5.scalar_product(v6))) < 1e-9

    # Use wrong type
    with pytest.raises(TypeError, match=r".* is not a Vector4.*"):
        Vector4(1, 1, 1, 1).scalar_product(0)


def test_multiply_by_scalar():
    """Test multiply_by_scalar() method."""
    v1 = Vector4(1, 1, 1, 1)
    # Multiply by 0
    assert v1.multiply_by_scalar(0) == Vector4(0, 0, 0, 0)

    # Multiply by int
    assert v1.multiply_by_scalar(2) == Vector4(2, 2, 2, 2)

    # Multiply by float
    assert v1.multiply_by_scalar(0.5) == Vector4(0.5, 0.5, 0.5, 0.5)

    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a float or int.*"):
        Vector4(1, 1, 1, 1).multiply_by_scalar("z")


def test_multiply_by_matrix():
    """Test multiply_by_matrix() method."""
    # Multiply by matrix
    mat = HomothetyMatrix4x4(2)
    mat2 = HomothetyMatrix4x4(0)
    mat3 = TranslationMatrix4x4(1, 2, 3)

    # Test 1
    v1 = Vector4(0, 3, 2, 1)

    assert v1.multiply_by_matrix(mat) == Vector4(0, 6, 4, 1)
    assert v1.multiply_by_matrix(mat2) == Vector4(0, 0, 0, 1)
    assert v1.multiply_by_matrix(mat3) == Vector4(1, 5, 5, 1)

    # Test 2
    v2 = Vector4(1, 2, 3, 4)

    assert v2.multiply_by_matrix(mat) == Vector4(2, 4, 6, 4)
    assert v2.multiply_by_matrix(mat2) == Vector4(0, 0, 0, 4)
    assert v2.multiply_by_matrix(mat3) == Vector4(5, 10, 15, 4)

    # Multiply by wrong type
    with pytest.raises(TypeError, match=r".* is not a Matrix4x4.*"):
        v1.multiply_by_matrix(v2)


def test_normalize():
    """Test normalize() method."""
    # Normalize vector
    assert Vector4(2, 4, 4, 0).normalize() == Vector4(1/3, 2/3, 2/3, 0)

    # Norm == 0
    with pytest.raises(ValueError, match=r"Cannot normalize a zero vector.*"):
        Vector4(0, 0, 0, 0).normalize()


def test_homogeneous_Vector4():
    """Test HomogeneousVector4 class."""
    assert HomogeneousVector4(1, 2, 3) == Vector4(1, 2, 3, 1)
