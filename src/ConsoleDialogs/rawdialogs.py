# -*- coding: utf-8 -*-
"""
=========================
ConsoleDialogs.rawdialogs
=========================

input/raw_input based dialogs
"""
from __future__ import print_function, unicode_literals, division, absolute_import

import functools
import sys
import textwrap

if sys.version_info < (3, 3):
    from backports.shutil_get_terminal_size import get_terminal_size
else:
    from shutil import get_terminal_size
    raw_input = input


class ConsoleIO(object):
    """Context manager and decorator that forces temporarily stdin, stdout and stderr to the console"""
    def __init__(self):
        self.mem_stdin, self.mem_stdout, self.mem_stderr = sys.stdin, sys.stdout, sys.stderr

    def __flush_out_streams(self):
        sys.stdout.flush()
        sys.stderr.flush()

    def __to_console(self):
        """Forces default IO to console"""
        self.__flush_out_streams()
        sys.stdin, sys.stdout, sys.stderr = sys.__stdin__, sys.__stdout__, sys.__stderr__

    def __to_previous(self):
        """Back to previous situation"""
        self.__flush_out_streams()
        sys.stdin, sys.stdout, sys.stderr = self.mem_stdin, self.mem_stdout, self.mem_stderr

    # Context manager
    def __enter__(self):
        self.__to_console()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__to_previous()

    # Decorator
    def __call__(self, callable_):
        @functools.wraps(callable_)
        def wrapper(*args, **kwargs):
            with self:
                return callable_(*args, **kwargs)
        return wrapper


def show_message(text):
    width = get_terminal_size().columns
    width -= 1
    text = textwrap.fill(text, width=width)
    print()
    print('-' * width)
    print(text)
    print('-' * width)


class MessageDialog(object):
    def __init__(self, message):
        self.message = message

    @ConsoleIO()
    def show(self):
        show_message(self.message)
        # raw_input("Hit [Return] to continue!")


class PassFailDialog(object):
    def __init__(self, message):
        self.message = message

    @ConsoleIO()
    def show(self):
        possible = {
            'p': False,
            'f': True
        }
        show_message(self.message)
        while True:
            result = raw_input('[P]ass or [f]ail? [P]')
            result = result.strip().lower()
            result = possible.get(result)
            if isinstance(result, bool):
                break
        return result
