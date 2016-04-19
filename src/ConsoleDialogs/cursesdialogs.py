# -*- coding: utf-8 -*-
"""
============================
ConsoleDialogs.cursesdialogs
============================

curses based dialogs
"""
from __future__ import print_function, unicode_literals, division, absolute_import

import contextlib
import curses
import time

@contextlib.contextmanager
def curses_ui():
    """Part of app in curses context
    """
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    try:
        yield stdscr
    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()


class MessageDialog(object):
    def __init__(self, message):
        self.message = message

    def show(self):
        with curses_ui() as stdscr:
            # FIXME: On continue ici
            maxy, maxx = stdscr.getmaxyx()
            screen = stdscr.subwin(maxy-1, maxx-1, 0, 0)
            screen.refresh()
            time.sleep(3.0)


class PassFailDialog(object):
    def __init__(self, message):
        self.message = message

    def show(self):
        pass


def test():
    # MessageDialog
    md = MessageDialog("Hello, this is the message")
    result = md.show()
    print(result)

if __name__ == '__main__':
    test()
