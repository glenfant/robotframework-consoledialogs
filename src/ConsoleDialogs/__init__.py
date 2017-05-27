# -*- coding: utf-8 -*-
"""
==============
ConsoleDialogs
==============

A pure console replacement for the Robot Framework Dialogs library.
"""
from __future__ import print_function, unicode_literals, division, absolute_import

import pkg_resources

from robot.api import logger

from .keywords import ConsoleKeywords

# PEP 396 style version marker
try:
    __version__ = pkg_resources.get_distribution('robotframework-consoledialogs').version
except:
    logger.warn("Could not get the package version from pkg_resources")
    __version__ = 'unknown'


class ConsoleDialogs(ConsoleKeywords):
    """A test library providing dialogs for interacting with users.

    `ConsoleDialogs` is a replacement for the `Dialogs` Robot Framework's
    standard library that provides means for pausing the test execution and
    getting input from users. The dialogs are slightly different depending on
    are tests run on Python or Jython but they provide the same functionality.

    Long lines in the provided messages are wrapped automatically since
    Robot Framework 2.8. If you want to wrap lines manually, you can add
    newlines using the `\\n` character sequence.

    The library has following two limitations:
    - It is not compatible with IronPython.
    - It cannot be used with timeouts on Python.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'
    ROBOT_LIBRARY_VERSION = __version__

