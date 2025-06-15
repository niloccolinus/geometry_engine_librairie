
from Mathy import Vector4, Matrix4x4


class Renderer3D:
    def __init__(self, vertices: list[Vector4], indices: list[int]):
        self.vertices = vertices  # Local-space geometry (before transform)
        self.indices = indices  # Indices of the vertices

    def draw(self, gameobject: 'GameObject'):
        transform_matrix = gameobject.transform.get_matrix()

        print(f"Rendering object: {gameobject.name}")
        for i, vertex in enumerate(self.vertices):
            world_vertex = vertex.multiply_by_matrix(transform_matrix)
            print(f"Vertex {i}: {world_vertex}")
