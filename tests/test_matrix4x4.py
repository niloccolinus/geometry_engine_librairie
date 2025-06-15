"""Tests for verifying proper Matrix functionality."""

import pytest
from Mathy import (
    Matrix4x4,
    TranslationMatrix4x4,
    RotationMatrix4x4_x,
    RotationMatrix4x4_y,
    RotationMatrix4x4_z,
    HomothetyMatrix4x4,
    deg, sin, cos
)

# Example matrix 0 (zero matrix)
matrix0 = Matrix4x4(
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
)

# Example matrix 1
matrix1 = Matrix4x4(
    1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 16
)

# Example matrix 2
matrix2 = Matrix4x4(
    16, 15, 14, 13,
    12, 11, 10, 9,
    8, 7, 6, 5,
    4, 3, 2, 1
)

# Example matrix 3
matrix3 = Matrix4x4(
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1
)


def test_repr():
    """Test __repr__() method."""
    assert matrix0.__repr__() == "Matrix4x4([\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0],\n [0, 0, 0, 0]\n])"  # noqa: E501
    assert matrix1.__repr__() == "Matrix4x4([\n [1, 2, 3, 4],\n [5, 6, 7 ,8],\n [9, 10, 11, 12],\n [13, 14, 15, 16]\n])"  # noqa: E501
    assert matrix2.__repr__() == "Matrix4x4([\n [13, 14, 15, 16],\n[12, 11, 10, 9],\n [8, 7, 6, 5],\n [4, 3, 2, 1]\n])"  # noqa: E501


def test_eq():
    """Test __eq__() method."""
    assert matrix0 == Matrix4x4(
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0
    )
    assert matrix1 != matrix2


def test_add():
    """Test add() method with valid and invalid inputs."""
    result = matrix0.add(matrix1)
    assert result == matrix1

    result = matrix1.add(matrix2)
    expected = Matrix4x4(
        17, 17, 17, 17,
        17, 17, 17, 17,
        17, 17, 17, 17,
        17, 17, 17, 17
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.add("not a matrix")


def test_prod_r():
    """Test prod_r() method."""
    assert matrix1.prod_r(0) == matrix0
    result = matrix1.prod_r(2)
    expected = Matrix4x4(
        2, 4, 6, 8,
        10, 12, 14, 16,
        18, 20, 22, 24,
        26, 28, 30, 32
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.prod_r("not a number")


def test_prod():
    """Test prod() method with valid and invalid inputs."""
    result = matrix1.prod(matrix2)
    expected = Matrix4x4(
        80, 70, 60, 50,
        240, 214, 188, 162,
        400, 358, 316, 274,
        560, 502, 444, 386
    )
    assert result == expected

    # Invalid type
    with pytest.raises(TypeError):
        matrix1.prod("invalid")


def test_determinant():
    """Test determinant() method."""
    assert matrix1.determinant() == 0
    m = Matrix4x4(
        0, 1, 0, 0,
        1, 0, 0, 1,
        1, 1, 1, 1,
        1, 1, 0, 0
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
    """Test TranslationMatrix4x4."""
    t = TranslationMatrix4x4(2, 3, 4)
    expected = Matrix4x4(
        1, 0, 0, 2,
        0, 1, 0, 3,
        0, 0, 1, 4,
        0, 0, 0, 1
    )
    assert t == expected


def test_rotation_matrix_x():
    """Test RotationMatrix4x4 for 45 degrees."""
    angle_deg = 45
    theta = deg(angle_deg)
    r = RotationMatrix4x4_x(angle_deg)
    expected = Matrix4x4(
        1, 0, 0, 0,
        0, cos(theta), -sin(theta), 0,
        0, sin(theta), cos(theta), 0,
        0, 0, 0, 1
        )
    for i in range(4):
        for j in range(4):
            diff = abs(r.matrix[i][j] - expected.matrix[i][j])
            assert diff < 1e-6, f"Rotation matrix mismatch at ({i},{j})"


def test_rotation_matrix_y():
    """Test RotationMatrix4x4 for 45 degrees."""
    angle_deg = 45
    theta = deg(angle_deg)
    r = RotationMatrix4x4_y(angle_deg)
    expected = Matrix4x4(
        cos(theta), 0, sin(theta), 0,
        0, 1, 0, 0,
        -sin(theta), 0, cos(theta), 0,
        0, 0, 0, 1
        )
    for i in range(4):
        for j in range(4):
            diff = abs(r.matrix[i][j] - expected.matrix[i][j])
            assert diff < 1e-6, f"Rotation matrix mismatch at ({i},{j})"


def test_rotation_matrix_z():
    """Test RotationMatrix4x4 for 45 degrees."""
    angle_deg = 45
    theta = deg(angle_deg)
    r = RotationMatrix4x4_z(angle_deg)
    expected = Matrix4x4(
        cos(theta), -sin(theta), 0, 0,
        sin(theta), cos(theta), 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
        )
    for i in range(3):
        for j in range(3):
            diff = abs(r.matrix[i][j] - expected.matrix[i][j])
            assert diff < 1e-6, f"Rotation matrix mismatch at ({i},{j})"


def test_homothety_matrix():
    """Test HomothetyMatrix4x4."""
    h = HomothetyMatrix4x4(2)
    expected = Matrix4x4(
        2, 0, 0, 0,
        0, 2, 0, 0,
        0, 0, 2, 0,
        0, 0, 0, 1
    )
    assert h == expected
