"""open-asimov.

Modular AI assistant backend with composable intelligence primitives.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

from openjarvis.sdk import Jarvis, JarvisSystem, MemoryHandle, SystemBuilder

for _dist_name in ("open-asimov", "openjarvis"):
    try:
        __version__ = _pkg_version(_dist_name)
        break
    except PackageNotFoundError:  # pragma: no cover — try compatibility name
        continue
else:  # pragma: no cover — uninstalled source tree
    __version__ = "0.0.0+unknown"

__all__ = ["Jarvis", "JarvisSystem", "MemoryHandle", "SystemBuilder", "__version__"]
