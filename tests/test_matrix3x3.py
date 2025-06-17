"""Tests for verifying proper Matrix functionality."""

import pytest
from Mathy import (
    Matrix3x3,
    TranslationMatrix3x3,
    RotationMatrix3x3,
    HomothetyMatrix3x3,
    rad, sin, cos
)

# Example matrix 0 (zero matrix)
matrix0 = Matrix3x3(
    0, 0, 0,
    0, 0, 0,
    0, 0, 0
)

# Example matrix 1
matrix1 = Matrix3x3(
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
)

# Example matrix 2
matrix2 = Matrix3x3(
    9, 8, 7,
    6, 5, 4,
    3, 2, 1
)

# Example matrix 3
matrix3 = Matrix3x3(
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
)


def test_repr():
    """Test __repr__() method."""
    assert matrix0.__repr__() == "Matrix3x3([\n [0, 0, 0],\n [0, 0, 0],\n [0, 0, 0]\n])"  # noqa: E501
    assert matrix1.__repr__() == "Matrix3x3([\n [1, 2, 3],\n [4, 5, 6],\n [7, 8, 9]\n])"  # noqa: E501
    assert matrix2.__repr__() == "Matrix3x3([\n [9, 8, 7],\n [6, 5, 4],\n [3, 2, 1]\n])"  # noqa: E501


def test_eq():
    """Test __eq__() method."""
    assert matrix0 == Matrix3x3(
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    )
    assert matrix1 != matrix2


def test_add():
    """Test add() method with valid and invalid inputs."""
    result = matrix0.add(matrix1)
    assert result == matrix1

    result = matrix1.add(matrix2)
    expected = Matrix3x3(
        10, 10, 10,
        10, 10, 10,
        10, 10, 10
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.add("not a matrix")


def test_prod_r():
    """Test prod_r() method."""
    assert matrix1.prod_r(0) == matrix0
    result = matrix1.prod_r(2)
    expected = Matrix3x3(
        2, 4, 6,
        8, 10, 12,
        14, 16, 18
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.prod_r("not a number")


def test_prod():
    """Test prod() method with valid and invalid inputs."""
    result = matrix1.prod(matrix2)
    expected = Matrix3x3(
        30, 24, 18,
        84, 69, 54,
        138, 114, 90
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.prod("invalid")


def test_determinant():
    """Test determinant() method."""
    assert matrix1.determinant() == 0
    m = Matrix3x3(
        1, 2, 3,
        0, 1, 4,
        5, 6, 0
    )
    assert abs(m.determinant() - 1) < 1e-6


def test_round():
    """Test roun() method."""
    assert matrix3.prod_r(10**(-10)).round(9) == matrix0
    assert matrix3.prod_r(10**(-9)).round(9) != matrix0
    # Invalid decimal : wrong type
    with pytest.raises(TypeError):
        matrix3.round("invalid")
    # Invalid decimal : wrong value
    with pytest.raises(ValueError):
        matrix3.round(-1)


def test_translation_matrix():
    """Test TranslationMatrix3x3."""
    t = TranslationMatrix3x3(2, 3)
    expected = Matrix3x3(
        1, 0, 2,
        0, 1, 3,
        0, 0, 1
    )
    assert t == expected


def test_rotation_matrix():
    """Test RotationMatrix3x3 for 45 degrees."""
    angle_deg = 45
    theta = rad(angle_deg)
    r = RotationMatrix3x3(angle_deg)
    expected = Matrix3x3(
        cos(theta), -sin(theta), 0,
        sin(theta), cos(theta), 0,
        0, 0, 1
    )
    for i in range(3):
        for j in range(3):
            diff = abs(r.matrix[i][j] - expected.matrix[i][j])
            assert diff < 1e-6, f"Rotation matrix mismatch at ({i},{j})"


def test_homothety_matrix():
    """Test HomothetyMatrix3x3."""
    h = HomothetyMatrix3x3(2)
    expected = Matrix3x3(
        2, 0, 0,
        0, 2, 0,
        0, 0, 1
    )
    assert h == expected
