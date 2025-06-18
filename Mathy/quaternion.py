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
