"""Defines a triangle class."""

import math


class Triangle:
    """A class to represent a triangle."""

    def __init__(
        self,
        p1: tuple[float, float],
        p2: tuple[float, float],
        p3: tuple[float, float]
    ):
        """
        Initialize a triangle with 3 vertices.

        Each point is a tuple (x, y).
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self) -> tuple[float, float, float]:
        """Return the lengths of the triangle's sides (a, b, c).

        a = length between p1 and p2
        b = length between p2 and p3
        c = length between p1 and p3
        """
        def distance(pA, pB):
            dx = pA[0] - pB[0]
            dy = pA[1] - pB[1]
            return math.sqrt(dx ** 2 + dy ** 2)

        a = distance(self.p1, self.p2)
        b = distance(self.p2, self.p3)
        c = distance(self.p1, self.p3)
        return a, b, c

    def perimeter(self) -> float:
        """Return the perimeter of the triangle."""
        a, b, c = self.side_lengths()
        return a + b + c

    def area(self) -> float:
        """Return the area of the triangle using Heron's formula."""
        if self.right_angled():
            # Sort to make sure the hypothenuse is last
            a, b, c = sorted(self.side_lengths())
            return (a * b) / 2
        a, b, c = self.side_lengths()
        s = (a + b + c) / 2  # semi-perimeter
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def right_angled(self) -> bool:
        """Check if the triangle is right-angled using Pythagorean theorem."""
        # Sort to make sure the hypothenuse is last
        a, b, c = sorted(self.side_lengths())
        # Use isclose to allow for small floating-point errors
        return math.isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9)

    def get_vertices(
        self
    ) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]]:
        """Return the three vertices of the triangle."""
        return self.p1, self.p2, self.p3

    def get_edges(
        self
    ) -> tuple[tuple[tuple[float, float], tuple[float, float]],
               tuple[tuple[float, float], tuple[float, float]],
               tuple[tuple[float, float], tuple[float, float]]]:
        """Return the three edges of the triangle."""
        return [
            (self.p1, self.p2),
            (self.p2, self.p3),
            (self.p3, self.p1)
        ]

    def circumcircle(self) -> tuple[tuple[float, float], float]:
        """Return the circumcenter and circumradius of the triangle."""
        ax, ay = self.p1
        bx, by = self.p2
        cx, cy = self.p3

        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if d == 0:
            return None, float('inf')

        ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay)
              + (cx**2 + cy**2) * (ay - by)) / d
        uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx)
              + (cx**2 + cy**2) * (bx - ax)) / d
        r = math.sqrt((ax - ux)**2 + (ay - uy)**2)

        return (ux, uy), r

    def is_point_in_circumcircle(self, point: tuple[float, float]) -> bool:
        """Check if a point is inside the circumcircle of the triangle."""
        circumcenter, circumradius = self.circumcircle()
        norm = math.sqrt(
            (point[0] - circumcenter[0])**2 + (point[1] - circumcenter[1])**2)
        return norm < circumradius
