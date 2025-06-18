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
            return Quaternion(
                        self.w * (other.w + other.x + other.y + other.z) +
                        self.x * (other.w + other.x + other.y + other.z) +
                        self.y * (other.w + other.x + other.y + other.z) +
                        self.z * (other.w + other.x + other.y + other.z))
        else:
            raise TypeError(f"{other} is not a Quaternion")
