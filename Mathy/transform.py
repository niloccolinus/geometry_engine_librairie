class Transform:
    def __init__(self, position=None, rotation=None, scale=None):
        from Mathy import Vector3
        self.position = position or Vector3(0, 0, 0)
        self.rotation = rotation or Vector3(0, 0, 0)
        self.scale = scale or Vector3(1, 1, 1)

    def get_matrix(self) -> 'Matrix4x4':
        from Mathy import Matrix4x4, TranslationMatrix4x4, RotationMatrix4x4, HomothetyMatrix4x4
        T = TranslationMatrix4x4(self.position)
        R = RotationMatrix4x4(self.rotation)
        S = HomothetyMatrix4x4(self.scale)
        return T.prod(R).prod(S)
