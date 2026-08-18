# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-collapse — Which term took this conjunction to zero?

One narrow problem. See :mod:`loomground_collapse.collapse` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .collapse import (
    ConstituentState,
    Constituent,
    state_to_verdict,
    collapse,
)

__all__ = [
    "__version__",
    "ConstituentState",
    "Constituent",
    "state_to_verdict",
    "collapse",
]
