"""Defines a Transform class containing a GameObject's geometry data."""


from Mathy import (TranslationMatrix4x4,
                   RotationMatrix4x4_x,
                   RotationMatrix4x4_y,
                   RotationMatrix4x4_z,
                   TotalRotationMatrix4x4,
                   HomothetyMatrix4x4,
                   AnisotropicMatrix4x4)


class Transform:
    """A class to represent a game object's position, rotation and scale."""

    def __init__(self):
        """Initialize a transform."""
        self.transform_matrix = HomothetyMatrix4x4(1)

    def translate(self, a, b, c):
        """Apply translation."""
        translation = TranslationMatrix4x4(a, b, c)
        self.transform_matrix = self.transform_matrix.prod(translation)

    def rotate(self, angle_x, angle_y, angle_z):
        """Apply rotation."""
        rot_x = RotationMatrix4x4_x(angle_x)
        rot_y = RotationMatrix4x4_y(angle_y)
        rot_z = RotationMatrix4x4_z(angle_z)
        rotation = TotalRotationMatrix4x4(rot_x, rot_y, rot_z)
        self.transform_matrix = self.transform_matrix.prod(rotation)

    def homothetic_scale(self, k):
        """Apply homothety."""
        homothety = HomothetyMatrix4x4(k)
        self.transform_matrix = self.transform_matrix.prod(homothety)

    def anisotropic_scale(self, sx, sy, sz):
        """Apply anisotropic scaling."""
        anisotropic = AnisotropicMatrix4x4(sx, sy, sz)
        self.transform_matrix = self.transform_matrix.prod(anisotropic)
