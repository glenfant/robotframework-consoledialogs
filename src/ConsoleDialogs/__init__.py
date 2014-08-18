# -*- coding: utf-8 -*-
"""
==============
ConsoleDialogs
==============

A pure console replacement for the Robot Framework Dialogs library.
"""

import sys
import logging
import pkg_resources

# Custom logger
LOG = logging.getLogger(name=__name__)
if sys.version_info < (2, 7):
    class NullHandler(logging.Handler):
        """Copied from Python 2.7 to avoid getting `No handlers could be found
        for logger "xxx"` http://bugs.python.org/issue16539
        """
        def handle(self, record):
            pass
        def emit(self, record):
            pass
        def createLock(self):
            self.lock = None
else:
    from logging import NullHandler

LOG.addHandler(NullHandler())

# PEP 396 style version marker
try:
    __version__ = pkg_resources.get_distribution(u'robotframework-consoledialogs').version
except:
    LOG.warning("Could not get the package version from pkg_resources")
    __version__ = 'unknown'

# FIXME: This is just for checking doctests setup. You may remove this function.
# See tests/test_doctests.py from this distro root
def identity(obj):
    """Returns the ``obj`` parameter itself

        >>> identity(5)
        5
        >>> foo = 2
        >>> identity(foo) is foo
        True
    """
    return obj
