# -*- coding: utf-8 -*-
"""We need to fake tkinter subset since importing the legacy dialog docstrings require tkinter"""


class Button:
    pass

Entry = Frame = Label = Listbox = TclError = Toplevel = Tk = Button
BOTH = END = LEFT = W = None
