# coding=utf-8
__author__ = 'Peter Wang'
__license__ = 'apache v2.0'
__version__ = '0.1.0'

import sys
if sys.version_info < (3, 0):
    from Queue import Empty, Full
else:
    from queue import Empty, Full

from .queue import Queue

__all__ = ["Queue", "Empty", "Full", "__author__",
           "__license__", "__version__"]
