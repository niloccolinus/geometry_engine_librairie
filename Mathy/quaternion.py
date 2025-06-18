"""A class to represent a quaternion."""

import math
from Mathy import Matrix4x4


class Quaternion:
    def __init__(self, 
                 w: float | int, 
                 x: float | int, 
                 y: float | int, 
                 z: float | int):
        """Initialize a quaternion with the given values."""
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    @property
    def norm(self) -> float:
        """Calculate the norm of the quaternion (accessible as a property)."""
        return (self.w**2 + self.x**2 + self.y**2 + self.z**2)**0.5

    @property
    def conjugate(self) -> 'Quaternion':
        """Calculate the conjugate of the quaternion."""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self) -> 'Quaternion':
        """Calculate the inverse of the quaternion."""
        return self.conjugate / self.norm**2

    def add(self, other: 'Quaternion') -> 'Quaternion':
        """Add two quaternions together and return a new Quaternion."""
        if isinstance(other, Quaternion):
            return Quaternion(self.w + other.w, self.x + other.x,
                              self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"{other} is not a Quaternion")

    def prod(self, other: 'Quaternion') -> 'Quaternion':
        """Multiply two quaternions together and return a new Quaternion."""
        if isinstance(other, Quaternion):
            w1, x1, y1, z1 = self.w, self.x, self.y, self.z
            w2, x2, y2, z2 = other.w, other.x, other.y, other.z

            w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
            x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
            y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
            z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2

            return Quaternion(w, x, y, z)
        else:
            raise TypeError(f"{other} is not a Quaternion")

    def euler_to_quaternion(angle_x, angle_y, angle_z) -> 'Quaternion':
        from Mathy import cos, sin
        q1 = Quaternion(cos(angle_x/2), sin(angle_x/2), 0, 0)
        q2 = Quaternion(cos(angle_y/2), 0, sin(angle_y/2), 0)
        q3 = Quaternion(cos(angle_z/2), 0, 0, sin(angle_z/2))

        return q3.prod(q2).prod(q1)

    def to_euler(self) -> tuple[float, float, float]:
        w, x, y, z = self
        angle_x = math.atan2(2(w*x + y*z), 1 - 2(x**2 + y**2))
        angle_y = math.asin(2(w*y - z*x))
        angle_z = math.atan2(2(w*z + x*y), 1 - 2(y**2 + z**2))

        return tuple[angle_x, angle_y, angle_z]

