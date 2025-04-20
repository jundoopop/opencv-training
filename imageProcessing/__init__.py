"""Compatibility shim for legacy imports.

This module aliases the new package ``opencv_training_pkg.image_processing``
so that code written with the old ``imageProcessing`` top‑level package keeps
working until everything is fully migrated.
"""
import importlib as _importlib
import sys as _sys

_pkg = _importlib.import_module("opencv_training_pkg.image_processing")
_sys.modules[__name__] = _pkg
