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
__version__ = "0.14.3"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple

from . import utils
from .client import *
from .color import *
from .enums import *
from .errors import *
from .item import *
from .iterators import *
from .sale import *
from .salefeed import *
from .transaction import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=14, micro=3, releaselevel="final", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
