"""
Skinport API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Skinport API.
:copyright: (c) 2022 PaxxPatriot
:license: MIT, see LICENSE for more details.
"""
__title__ = "skinport"
__author__ = "PaxxPatriot"
__license__ = "MIT"
__copyright__ = "Copyright 2022 PaxxPatriot"
__version__ = "0.2.2"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .client import *
from .enums import *
from .errors import *
from .item import *
from .sale import *
from .transaction import *
from .iterators import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=2, micro=2, releaselevel="final", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
