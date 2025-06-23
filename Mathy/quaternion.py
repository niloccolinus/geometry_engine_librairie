"""A class to represent a quaternion."""

import math
from Mathy import Matrix4x4


class Quaternion:
    """Define a quaternion class."""

    def __init__(self,
                 w: float | int,
                 x: float | int,
                 y: float | int,
                 z: float | int):
        """Initialize a quaternion with the given values."""
        if all(isinstance(i, (int, float)) for i in [x, y, z, w]):
            self.w = w
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError("All components must be floats or ints.")

    def __eq__(self, other: object) -> bool:
        """Check if two quaternions are equal (with float tolerance)."""
        if not isinstance(other, Quaternion):
            return False
        return (
            abs(self.w - other.w) < 1e-9 and
            abs(self.x - other.x) < 1e-9 and
            abs(self.y - other.y) < 1e-9 and
            abs(self.z - other.z) < 1e-9
        )

    def __truediv__(self, scalar: float | int) -> 'Quaternion':
        """Divide the quaternion by a scalar."""
        if abs(scalar) < 1e-9:
            raise ZeroDivisionError("Cannot divide by zero.")
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"{scalar} is not a number.")
        return Quaternion(
            self.w / scalar,
            self.x / scalar,
            self.y / scalar,
            self.z / scalar
        )

    @property
    def norm(self) -> float:
        """Calculate the norm of the quaternion (accessible as a property)."""
        return (self.w**2 + self.x**2 + self.y**2 + self.z**2)**0.5

    @property
    def conjugate(self) -> 'Quaternion':
        """Calculate the conjugate of the quaternion."""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    @property
    def inverse(self) -> 'Quaternion':
        """Calculate the inverse of the quaternion."""
        if self == Quaternion(0, 0, 0, 0):
            raise ValueError("Null quaternion is not invertible.")
        return self.conjugate / self.norm**2

    def normalize(self) -> 'Quaternion':
        """Return a normalized (unit) quaternion with the same orientation."""
        n = self.norm
        if abs(n) < 1e-9:
            raise ValueError("Cannot normalize a zero quaternion.")
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n)

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
        """Convert Euler angles (in radians) to a quaternion."""
        from Mathy import cos, sin

        qx = Quaternion(cos(angle_x/2), sin(angle_x/2), 0, 0)
        qy = Quaternion(cos(angle_y/2), 0, sin(angle_y/2), 0)
        qz = Quaternion(cos(angle_z/2), 0, 0, sin(angle_z/2))

        return qz.prod(qy).prod(qx)  # q = qz * qy * qx (Z-Y-X order)

    def to_euler(self) -> tuple[float, float, float]:
        """Convert quaternion to Euler angles."""
        w, x, y, z = self.w, self.x, self.y, self.z
        angle_x = math.atan2(2*(w*x + y*z), 1 - 2*(x**2 + y**2))  # roll
        angle_y = math.asin(2*(w*y - z*x))                        # pitch
        angle_z = math.atan2(2*(w*z + x*y), 1 - 2*(y**2 + z**2))  # yaw

        return (angle_x, angle_y, angle_z)

    def to_rotation_matrix(self) -> 'Matrix4x4':
        """Convert quaternion to rotation matrix."""
        from Mathy import Matrix4x4

        q = self.normalize()
        w, x, y, z = q.w, q.x, q.y, q.z

        return Matrix4x4(
            1 - 2*(y**2 + z**2), 2*(x*y - w*z),       2*(x*z + w*y),       0,
            2*(x*y + w*z),       1 - 2*(x**2 + z**2), 2*(y*z - w*x),       0,
            2*(x*z - w*y),       2*(y*z + w*x),       1 - 2*(x**2 + y**2), 0,
            0,                   0,                   0,                   1
        )
