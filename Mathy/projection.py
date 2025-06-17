"""A class to handle 3D to screen projection."""

from Mathy import Vector4, Matrix4x4
from Mathy.math_utils import pi, tan


class Projection:
    """
    A projection system for transforming 3D coordinates into a 2D plane.

    For a vertex in camera space, multiplying by the projection matrix will
    return a new vector in clip space, which can then be transformed
    to screen space.
    """

    def __init__(self, width, height, fov, near_plane, far_plane):
        """Initialize the projection."""
        self.width = width
        self.height = height
        # Aspect ratio of the viewport (width/height)
        self.aspect_ratio = width / height
        self.fov = fov  # Field of view in degrees
        self.fovRad = fov * (pi / 180)
        self.near_plane = near_plane  # Near clipping plane distance
        self.far_plane = far_plane  # Far clipping plane distance

    def get_projection_matrix(self):
        """Return a projection matrix to switch from camera to clip space."""
        f = 1 / tan(self.fovRad / 2)
        nf = 1 / (self.near_plane - self.far_plane)

        projection_matrix = Matrix4x4(
            f / self.aspect_ratio, 0, 0, 0,
            0, f, 0, 0,
            0, 0, (self.far_plane + self.near_plane) * nf, 2 * self.far_plane * self.near_plane * nf,  # noqa: E501
            0, 0, -1, 0
        )

        return projection_matrix

    def get_screen_coordinates(self, vertex: Vector4):
        """
        Convert a vertex in clip space to NDC*, then screen coordinates.

        The vertex should be in clip space (after projection).
        NDC* coordinates are Normalized Device Coordinates,
        which range from -1 to 1.
        """
        # Perform perspective division
        if abs(vertex.w) > 1e-9:
            x_ndc = vertex.x / vertex.w
            y_ndc = vertex.y / vertex.w
            z = vertex.z / vertex.w
        else:
            x_ndc, y_ndc, z = 0, 0, 0

        # Convert to screen coordinates
        x_screen = (x_ndc + 1)/2 * self.width
        y_screen = (1 - y_ndc)/2 * self.height

        return Vector4(x_screen, y_screen, z, 1)
