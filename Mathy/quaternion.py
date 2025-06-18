"""A class to represent a quaternion."""


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
