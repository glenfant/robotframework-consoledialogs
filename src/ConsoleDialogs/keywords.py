# -*- coding: utf-8 -*-
"""
=======================
ConsoleDialogs.keywords
=======================

Provide the keywords
"""
from __future__ import print_function, unicode_literals, division, absolute_import

import os

import robot.libraries.Dialogs as orig_dialogs

try:
    import curses
    USE_CURSES = True
except ImportError:
    USE_CURSES = False

USE_CURSES = 'RF_INLINE_DIALOGS' not in os.environ

if USE_CURSES:
    from .cursesdialogs import MessageDialog, PassFailDialog
else:
    from .rawdialogs import MessageDialog, PassFailDialog


class ConsoleKeywords(object):
    def pause_execution(self, message='Test execution paused.'):
        # """Pauses test execution until user hits `Return` key.
        #
        # `message` is the message shown in the dialog.
        # """
        MessageDialog(message).show()

    def execute_manual_step(self, message, default_error=''):
        # """Pauses test execution until user sets the keyword status.
        #
        # User can press either `PASS` or `FAIL` button. In the latter case execution
        # fails and an additional dialog is opened for defining the error message.
        #
        # `message` is the instruction shown in the initial dialog and
        # `default_error` is the default value shown in the possible error message
        # dialog.
        # """
        if not PassFailDialog(message).show():
            msg = self.get_value_from_user('Give error message:', default_error)
            raise AssertionError(msg)


    def get_value_from_user(self, message, default_value='', hidden=False):
        # """Pauses test execution and asks user to input a value.
        #
        # Value typed by the user, or the possible default value, is returned.
        # Returning an empty value is fine, but pressing `Cancel` fails the keyword.
        #
        # `message` is the instruction shown in the dialog and `default_value` is
        # the possible default value shown in the input field.
        #
        # If `hidden` is given any true value, such as any non-empty string, the value
        # typed by the user is hidden. This is a new feature in Robot Framework 2.8.4.
        #
        # Example:
        # | ${username} = | Get Value From User | Input user name | default    |
        # | ${password} = | Get Value From User | Input password  | hidden=yes |
        # """
        pass

    def get_selection_from_user(self, message, *values):
        # """Pauses test execution and asks user to select a value.
        #
        # The selected value is returned. Pressing `Cancel` fails the keyword.
        #
        # `message` is the instruction shown in the dialog and `values` are
        # the options given to the user.
        #
        # Example:
        # | ${username} = | Get Selection From User | Select user name | user1 | user2 | admin |
        # """
        pass

# Fixing docstrings

for keyword in ('pause_execution', 'execute_manual_step', 'get_value_from_user', 'get_selection_from_user'):
    getattr(ConsoleKeywords, keyword).__func__.__doc__ = getattr(orig_dialogs, keyword).__doc__


# ConsoleKeywords.pause_execution.__func__.__doc__ = orig_dialogs.pause_execution.__doc__
# ConsoleKeywords.execute_manual_step.__func__.__doc__ = orig_dialogs.execute_manual_step.__doc__
# ConsoleKeywords.get_value_from_user.__func__.__doc__ = orig_dialogs.get_value_from_user.__doc__
# ConsoleKeywords.get_selection_from_user.__func__.__doc__ = orig_dialogs.get_selection_from_user.__doc__
