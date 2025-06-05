"""Marks the current directory as a package."""

from .math_utils import pi, factorial, deg, sin, cos
from .renderer import Renderer
from .vector2 import Vector2
from .triangle import Triangle
from .matrix2x2 import Matrix2x2
from .vector3 import Vector3
from .vector3 import HomogeneousVector3
from .matrix3x3 import Matrix3x3
from .matrix3x3 import TranslationMatrix3x3
from .matrix3x3 import RotationMatrix3x3
from .matrix3x3 import HomothetyMatrix3x3
from .barycentric import barycentric_coordinates
from .renderer3d import Renderer3D
from .transform import Transform
from .gameobject import GameObject

__all__ = [
    "Renderer",
    "Vector2",
    "Triangle",
    "Matrix2x2",
    "Matrix3x3",
    "TranslationMatrix3x3",
    "RotationMatrix3x3",
    "HomothetyMatrix3x3",
    "pi",
    "factorial",
    "deg",
    "sin",
    "cos",
    "Vector3",
    "HomogeneousVector3",
    "barycentric_coordinates",
    "Renderer3D",
    "Transform",
    "GameObject"
]
