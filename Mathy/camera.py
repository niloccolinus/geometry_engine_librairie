"""A class to represent a camera in a 3D scene."""

from Mathy import Vector3, Vector4, Matrix4x4


class Camera:
    """Represents a simple 3D camera for view transformations."""

    def __init__(self, position:  Vector3 = None, target: Vector3 = None, up: Vector3 = None):  # noqa: E501
        """Initialize a camera class."""
        self.position = position or Vector3(0, 0, 0)
        # Default target in negative Z direction (conventional)
        self.target = Vector3(target.x, target.y, -target.z) or Vector3(0, 0, -1)  # noqa: E501
        # Default up vector pointing in positive Y direction
        self.up = up or Vector3(0, 1, 0)

    def get_view_matrix(self):
        """Get view matrix (camera coordinates)."""
        # Compute forward, right, and up vectors
        forward = self.target.subtract(self.position).normalize()
        right = self.up.cross_product(forward).normalize()
        up = forward.cross_product(right).normalize()

        # The rotation aligns the camera's view direction
        # with the negative Z-axis
        rot = Matrix4x4(
            right.x, up.x, -forward.x, 0,
            right.y, up.y, -forward.y, 0,
            right.z, up.z, -forward.z, 0,
            0, 0, 0, 1
        )
        # The translation moves the world so the camera is at the origin
        translation = Matrix4x4(
            1, 0, 0, -self.position.x,
            0, 1, 0, -self.position.y,
            0, 0, 1, -self.position.z,
            0, 0, 0, 1
        )

        # Combine rotation and translation to get the view matrix
        view_matrix = rot.prod(translation)

        return view_matrix

    def look_at(self, target: Vector3):
        """Set the camera to look at a specific target point in 3D space."""
        self.target = target
        return self.get_view_matrix()

    def get_vertex_in_camera_space(self, vertex: Vector3):
        """
        Transform a vertex from world space to camera space.

        The vertex should be in world coordinates.
        """
        view_matrix = self.get_view_matrix()
        # Convert the vertex to a 4D vector for matrix multiplication
        world_vertex = Vector4(vertex.x, vertex.y, vertex.z, 1)
        # Apply the view matrix to the vertex
        camera_space_vertex = world_vertex.multiply_by_matrix(view_matrix)
        return camera_space_vertex
