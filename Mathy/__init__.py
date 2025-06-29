"""Marks the current directory as a package."""

from .math_utils import pi, factorial, deg_to_rad, sin, cos, tan, is_close
from .vector2 import Vector2
from .vector3 import Vector3
from .triangle import Triangle
from .triangle import Triangle3D
from .matrix2x2 import Matrix2x2
from .vector3 import HomogeneousVector3
from .matrix3x3 import Matrix3x3
from .matrix3x3 import TranslationMatrix3x3
from .matrix3x3 import RotationMatrix3x3
from .matrix3x3 import HomothetyMatrix3x3
from .matrix4x4 import Matrix4x4
from .matrix4x4 import TranslationMatrix4x4
from .matrix4x4 import RotationMatrix4x4_x
from .matrix4x4 import RotationMatrix4x4_y
from .matrix4x4 import RotationMatrix4x4_z
from .matrix4x4 import HomothetyMatrix4x4
from .barycentric import barycentric_coordinates
from .texture import gengar_tex
from .vector4 import Vector4
from .vector4 import HomogeneousVector4
from .matrix4x4 import AnisotropicMatrix4x4
from .matrix4x4 import TotalRotationMatrix4x4
from .renderer3d import Renderer3D
from .quaternion import Quaternion
from .transform import Transform
from .gameobject import GameObject
from .renderer import Renderer
from .gameobject import Cube
from .camera import Camera
from .projection import Projection
from .gameobject import Airplane

__all__ = [
    "Vector2",
    "Triangle",
    "Matrix2x2",
    "Matrix3x3",
    "TranslationMatrix3x3",
    "RotationMatrix3x3",
    "HomothetyMatrix3x3",
    "gengar_tex",
    "pi",
    "factorial",
    "deg_to_rad",
    "sin",
    "cos",
    "tan",
    "is_close",
    "Vector3",
    "HomogeneousVector3",
    "barycentric_coordinates",
    "Vector4",
    "HomogeneousVector4",
    "Matrix4x4",
    "TranslationMatrix4x4",
    "HomothetyMatrix4x4",
    "RotationMatrix4x4_x",
    "RotationMatrix4x4_y",
    "RotationMatrix4x4_z",
    "AnisotropicMatrix4x4",
    "TotalRotationMatrix4x4",
    "Renderer3D",
    "Transform",
    "GameObject",
    "Renderer",
    "Cube",
    "Camera",
    "Projection",
    "Quaternion",
    "Airplane",
    "Triangle3D"
]
