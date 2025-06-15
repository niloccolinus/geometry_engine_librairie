from Mathy import Vector4, Matrix4x4
from Mathy.math_utils import pi, tan

class Projection:
    """
    Represents a projection system for transforming 3D coordinates into a 2D plane.
    For a vertex in camera space, multiplying by the projection matrix will return
    a new vector in clip space, which can then be transformed to screen space.
    """

    def __init__(self, aspect_ratio, fov, near_plane, far_plane):
        self.aspect_ratio = aspect_ratio # Aspect ratio of the viewport (width/height)
        self.fov = fov # Field of view in degrees
        self.fovRad = fov * (pi / 180)
        self.near_plane = near_plane # Near clipping plane distance
        self.far_plane = far_plane  # Far clipping plane distance

    def get_projection_matrix(self):
        """
        Returns a 4x4 projection matrix for transforming camera space coordinates to clip space.
        """
        pass