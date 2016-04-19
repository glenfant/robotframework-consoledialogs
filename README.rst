==============
ConsoleDialogs
==============

A pure console replacement for the Robot Framework Dialogs library that uses
curses when installed, and otherwise falls back to ``raw_input(...)`` based
dialogs.

ConsoleDialogs has exactly the same API as the builtin `Dialogs library
<http://robotframework.org/robotframework/latest/libraries/Dialogs.html>`_.

Installation
============

.. code:: console

   pip install robotframework-consoledialogs

Usage
=====

.. code:: robotframework

   *** Settings ***
   Library  ConsoleDialogs

   *** Test Cases ***
   Test Manual Step
       Execute Manual Step

   Test Selection From User
       ${username}=     Get Selection From User     Select user name    user1   user2   admin

   Test Value From User
       ${value}=        Get Value From User     Provide a name      default value
       ${secret}=       Get Value From User     Provide a password  hidden=yes

   Test pause Execution
       Pause Execution
       Pause Execution  message=Execution stopped. Hit [Return] to continue.

Developer notes
===============

Please use a virtualenv to maintain this package, but I should not need to say
that.

Grab the source from the SCM repository:

.. code:: console

   $ python setup.py develop
   $ easy_install ConsoleDialogs[dev]

Run the tests:

.. code:: console

   $ python setup.py test

Links
=====

PyPI

  https://pypi.python.org/pypi/robotframework-consoledialogs

Source code

  https://github.com/glenfant/robotframework-consoledialogs

Issues tracker

  https://github.com/glenfant/robotframework-consoledialogs/issues
