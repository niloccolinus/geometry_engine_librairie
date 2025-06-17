"""A function to compute barycentric coordinates."""

from Mathy import Vector3


def barycentric_coordinates(
    P: Vector3,
    A: Vector3,
    B: Vector3,
    C: Vector3
) -> tuple[float, float, float]:
    """
    Compute barycentric coordinates.

    We look at the barycentric coordinates (lambda_A, lambda_B, lambda_C)
    of point P in the triangle defined by points A, B, C.

    Returns (λA, λB, λC) such that:
        P = λA * A + λB * B + λC * C
        with λA + λB + λC = 1
    """
    # Extract the coordinates of each point
    x, y = P.x, P.y
    xA, yA = A.x, A.y
    xB, yB = B.x, B.y
    xC, yC = C.x, C.y

    # Compute the determinant of the system
    det = (xA - xC)*(yB - yC) - (xB - xC)*(yA - yC)
    if abs(det) < 1e-9:
        raise ValueError("Degenerate triangle: points are collinear")

    # Apply Cramer's rule to compute λA and λB
    lambda_A = ((x - xC)*(yB - yC) - (xB - xC)*(y - yC)) / det
    lambda_B = ((xA - xC)*(y - yC) - (x - xC)*(yA - yC)) / det
    # Compute λC knowing that λA + λB + λC = 1
    lambda_C = 1 - lambda_A - lambda_B

    return (lambda_A, lambda_B, lambda_C)
