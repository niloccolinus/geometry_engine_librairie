"""Tests for verifying proper Quaternion functionality."""

from Mathy import Quaternion, is_close, deg_to_rad, cos, sin
import pytest


def test_constructor():
    """Test arguments' types for Quaternion constructor."""
    # Ints
    Quaternion(1, 2, 3, 4)
    # Floats
    Quaternion(1.0, 2.0, 3.0, 4.0)
    # Floats and ints
    Quaternion(1, 2.0, 3, 4.0)
    # Invalid types
    with pytest.raises(TypeError, match=r".* must be floats or ints.*"):
        Quaternion(0, "a", None, [])


def test_norm():
    """Test norm() method."""
    # Norm zero
    assert is_close(Quaternion(0, 0, 0, 0).norm, 0.0)
    # Norm positive coordinates
    assert is_close(Quaternion(2, 4, 4, 0).norm, 6.0)
    # Norm negative coordinates
    assert is_close(Quaternion(-2, -4, 4, 0).norm, 6.0)


def test_normalize():
    """Test normalize() method."""
    # Normalize quaternion
    assert Quaternion(2, 4, 4, 0).normalize() == Quaternion(1/3, 2/3, 2/3, 0)
    # Norm == 0
    with pytest.raises(ValueError, match=r"Cannot normalize a zero quaternion.*"):  # noqa: E501
        Quaternion(0, 0, 0, 0).normalize()


def test_conjugate():
    """Test conjugate() method."""
    assert Quaternion(1, 2, 3, 4).conjugate == Quaternion(1, -2, -3, -4)


def test_inverse():
    """Test inverse() method."""
    q = Quaternion(1, 2, 3, 4)
    assert q.inverse == q.conjugate / q.norm**2


def test_euler_to_quaternion():
    """Test euler_to_quaternion() method."""
    angles = (deg_to_rad(30), deg_to_rad(45), deg_to_rad(60))
    q = Quaternion.euler_to_quaternion(*angles)

    assert is_close(q.norm, 1.0)


def test_quaternion_to_euler():
    """Test to_euler() method."""
    # Quaternion representing rotation of 90° (pi/2 rad) around Z axis
    # cos(θ/2), 0, 0, sin(θ/2)
    q = Quaternion(cos(deg_to_rad(45)), 0, 0, sin(deg_to_rad(45)))  
    angles = q.to_euler()

    expected_x = 0  # no roll
    expected_y = 0  # no pitch
    expected_z = deg_to_rad(90)  # yaw of 90 degrees

    assert is_close(angles[0], expected_x)
    assert is_close(angles[1], expected_y)
    assert is_close(angles[2], expected_z)
