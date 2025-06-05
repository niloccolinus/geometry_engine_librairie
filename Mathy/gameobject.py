from Mathy import Transform, Renderer3D


class GameObject:
    """
    Represents a 3D object in the scene with a transform and a renderer.
    """

    def __init__(self, name="GameObject", vertices=None):
        self.name = name
        self.transform = Transform()
        self.renderer = Renderer3D(vertices or [])
