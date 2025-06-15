"""Defines a Transform class containing a GameObject's geometry data."""

from Mathy import HomogeneousVector4, Matrix4x4


class Transform:
    """A class to represent a game object's position, rotation and scale."""

    def __init__(self, position=HomogeneousVector4(0, 0, 0),
                 rotation=0, scale=1):
        """Initialize a transform."""
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def get_matrix(self) -> 'Matrix4x4':
        from Mathy import (TranslationMatrix4x4,
                           RotationMatrix4x4,
                           HomothetyMatrix4x4)
        a, b, c = self.position.x, self.position.y, self.position.z
        T = TranslationMatrix4x4(a, b, c)
        R = RotationMatrix4x4(self.rotation)
        S = HomothetyMatrix4x4(self.scale)
        return T.prod(R).prod(S)
