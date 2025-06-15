from Mathy import Vector3

class Camera:
    """
    Represents a simple 3D camera for view transformations.
    """

    def __init__(self, position:  Vector3 = None, target: Vector3 = None, up: Vector3 = None):
        self.position = position or Vector3(0, 0, 0)
        # Default target in negative Z direction (conventional)
        self.target = target or Vector3(0, 0, -1)
        # Default up vector pointing in positive Y direction
        self.up = up or Vector3(0, 1, 0)

    def get_view_matrix(self):
        # Compute forward, right, and up vectors
        forward = self.target.subtract(self.position).normalize()
        right = self.up.cross_product(forward).normalize()
        up = forward.cross_product(right).normalize()

        # Create a 4x4 view matrix
        pass