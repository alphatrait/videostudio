# framework/__init__.py

from .elements import StaticAsset, DynamicAsset, TextElement
from .manipulators import MANIPULATORS, register_manipulator

__all__ = ['Canvas', 'StaticAsset', 'DynamicAsset', 'TextElement', 'MANIPULATORS', 'register_manipulator']
