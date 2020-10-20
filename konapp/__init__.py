"""
    konapp
    ~~~~~

    A microframework for clear and ordered console applications. Inspired by Flask.

    The name is the worst idea ever and comes from (Console -> Konsole) + app.
"""

# expose these objects as public interfaces
from .app import App
from .blueprint import Blueprint

__version__ = "0.0.1"
