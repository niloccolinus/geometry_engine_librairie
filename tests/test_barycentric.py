"""Tests for verifying barycentric coordinates behave as expected."""

from Mathy import Vector3, barycentric_coordinates


def test_barycentric_coordinates():
    """Run unit tests for barycentric class."""
    A = Vector3(0, 0, 0)
    B = Vector3(1, 0, 0)
    C = Vector3(0, 1, 0)

    # Test 1: Centroid (should be (1/3, 1/3, 1/3))
    P1 = Vector3(1/3, 1/3, 0)
    u, v, w = barycentric_coordinates(P1, A, B, C)
    assert abs(u - 1/3) < 1e-6, f"Expected u=1/3, got {u}"
    assert abs(v - 1/3) < 1e-6, f"Expected v=1/3, got {v}"
    assert abs(w - 1/3) < 1e-6, f"Expected w=1/3, got {w}"

    # Test 2: At vertex A (should be (1, 0, 0))
    P2 = A
    u, v, w = barycentric_coordinates(P2, A, B, C)
    assert abs(u - 1.0) < 1e-6 and abs(v) < 1e-6 and abs(w) < 1e-6

    # Test 3: At vertex B (should be (0, 1, 0))
    P3 = B
    u, v, w = barycentric_coordinates(P3, A, B, C)
    assert abs(u) < 1e-6 and abs(v - 1.0) < 1e-6 and abs(w) < 1e-6

    # Test 4: At vertex C (should be (0, 0, 1))
    P4 = C
    u, v, w = barycentric_coordinates(P4, A, B, C)
    assert abs(u) < 1e-6 and abs(v) < 1e-6 and abs(w - 1.0) < 1e-6

    # Test 5: Point outside the triangle
    # (should have at least one negative barycentric coordinate)
    P5 = Vector3(-0.5, -0.5, 0)
    u, v, w = barycentric_coordinates(P5, A, B, C)
    assert u < 0 or v < 0 or w < 0, f"Expected at least one negative coordinate for point outside, got {(u, v, w)}"  # noqa: E501

    # Test 6: Degenerate triangle (collinear points, should raise ValueError)
    A_col = Vector3(0, 0, 0)
    B_col = Vector3(1, 1, 0)
    C_col = Vector3(2, 2, 0)  # Points are collinear

    try:
        barycentric_coordinates(Vector3(1, 1, 0), A_col, B_col, C_col)
        assert False, "Expected ValueError for degenerate triangle"
    except ValueError as e:
        assert str(e) == "Degenerate triangle: points are collinear"

    print("All tests passed.")


if __name__ == "__main__":
    test_barycentric_coordinates()
