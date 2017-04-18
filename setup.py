# -*- coding: utf-8 -*-
"""
==============
ConsoleDialogs
==============

A pure console replacement for the Robot Framework Dialogs library.
"""

import os
import sys
from setuptools import setup, find_packages

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))


def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',), ('CHANGES.rst',))]
    )
install_requires = ['setuptools', 'robotframework']
if sys.version_info < (3, 3):
    install_requires.append('backports.shutil_get_terminal_size')
dev_require = []
if sys.version_info < (2, 7):
    dev_require += ['unittest2']


setup(name='robotframework-consoledialogs',
      version=version,
      description="A pure console replacement for the Robot Framework Dialogs library.",
      long_description=long_description,
      classifiers=[
          "Framework :: Robot Framework",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Environment :: Console :: Curses",
          "Operating System :: OS Independent"
          ],
      keywords='robotframework dialogs ui',
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://pypi.python.org/pypi/robotframework-consoledialogs',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'dev': dev_require
      })
