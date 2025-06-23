"""Tests for the Triangle class."""


from Mathy import Triangle, Triangle3D, math_utils

# Example triangle 1
triangle1 = Triangle([0, 0], [0, 1], [1, 0])
# Example triangle 2
triangle2 = Triangle([-1, 0], [0, 1], [1, 0])
# Example triangle 3
triangle3 = Triangle([-2.5, 0], [0, 5.5], [2.5, 0])


def test_side_lengths():
    """Test side_lengths() method."""
    # Lengths triangle 1
    assert triangle1.side_lengths() == (
        1.0, math_utils.root(2), 1.0)
    # Lengths triangle 2
    assert triangle2.side_lengths() == (
        math_utils.root(2), math_utils.root(2), 2.0)
    # Lengths triangle 3
    assert triangle3.side_lengths() == (
        math_utils.root(36.5), math_utils.root(36.5), 5.0)


def test_perimeter():
    """Test perimeter() method."""
    # Perimeter triangle 1
    assert triangle1.perimeter() == float(2 + math_utils.root(2))
    # Perimeter triangle 2
    assert triangle2.perimeter() == float(2 + math_utils.root(2) * 2)
    # Perimeter triangle 3
    assert triangle3.perimeter() == float(5 + math_utils.root(36.5) * 2)


def test_area():
    """Test area() method."""
    # Area triangle 1
    assert triangle1.area() == 0.5
    # Area triangle 2
    # Use is_close to allow for small floating-point errors
    assert math_utils.is_close(triangle2.area(), 1.0)
    # Area triangle 3
    # Use is_close to allow for small floating-point errors
    assert math_utils.is_close(triangle3.area(), 13.75)


def test_right_angled():
    """Test right_angled() method."""
    # Test right-angled triangle 1
    assert triangle1.right_angled() == 1
    # Test right-angled triangle 2
    assert triangle2.right_angled() == 1
    # Test non-right-angled triangle 3
    assert triangle3.right_angled() == 0


def test_get_vertices():
    """Test get_vertices() method."""
    # Vertices triangle 1
    assert triangle1.get_vertices() == ([0, 0], [0, 1], [1, 0])
    # Vertices triangle 2
    assert triangle2.get_vertices() == ([-1, 0], [0, 1], [1, 0])
    # Vertices triangle 3
    assert triangle3.get_vertices() == ([-2.5, 0], [0, 5.5], [2.5, 0])


# Triangle 3D Tests Unitaires
# Example triangle 4
triangle4 = Triangle3D([0, 0, 1], [0, 1, 0], [1, 0, 0])
# Example triangle 5
triangle5 = Triangle3D([-1, 0, 0], [0, 0, 1], [1, 0, 0])
# Example triangle 6
triangle6 = Triangle3D([0, -2.5, 0], [0, 0, 5.5], [2.5, 0, 0])


def test_side_lengths_3d():
    """Test side_lengths() method."""
    # Lengths triangle 4
    # assert triangle4.side_lengths() == (
    #     math_utils.root(2), math_utils.root(2), math_utils.root(2))
    # Lengths triangle 5
    assert triangle5.side_lengths() == (
        math_utils.root(2), math_utils.root(2), 2.0)
    # Lengths triangle 6
    assert triangle6.side_lengths() == (
        math_utils.root(36.5), math_utils.root(36.5), math_utils.root(12.5))


def test_perimeter_3d():
    """Test perimeter() method."""
    # Perimeter triangle 4
    assert triangle4.perimeter() == float(
        math_utils.root(2) * 3)
    # Perimeter triangle 5
    assert triangle5.perimeter() == float(
        2 + math_utils.root(2) * 2)
    # Perimeter triangle 6
    assert triangle6.perimeter() == float(
        math_utils.root(12.5) + math_utils.root(36.5) * 2)


def test_area_3d():
    """Test area() method."""
    # Area triangle 4
    assert math_utils.is_close(triangle4.area(), 0.87, 1e-02)
    # Area triangle 5
    # Use is_close to allow for small floating-point errors
    assert math_utils.is_close(triangle5.area(), 1.0)
    # Area triangle 6
    # Use is_close to allow for small floating-point errors
    assert math_utils.is_close(triangle6.area(), 10.21, 1e-02)


def test_right_angled_3d():
    """Test right_angled() method."""
    # Test right-angled triangle 4
    assert triangle4.right_angled() == 0
    # Test right-angled triangle 5
    assert triangle5.right_angled() == 1
    # Test non-right-angled triangle 6
    assert triangle6.right_angled() == 0


def test_get_vertices_3d():
    """Test get_vertices() method."""
    # Vertices triangle 4
    assert triangle4.get_vertices() == ([0, 0, 1], [0, 1, 0], [1, 0, 0])
    # Vertices triangle 5
    assert triangle5.get_vertices() == ([-1, 0, 0], [0, 0, 1], [1, 0, 0])
    # Vertices triangle 6
    assert triangle6.get_vertices() == ([0, -2.5, 0], [0, 0, 5.5], [2.5, 0, 0])
