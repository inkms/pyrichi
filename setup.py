#!/usr/bin/env python

from distutils.core import setup

setup(name='Pyrichi',
      version='0.1',
      description='Python Distribution Utilities',
      author='Iñaki Martín Soroa',
      author_email='i.martin.soroa@gmail.com',
      url='https://www.python.org/sigs/hihi/',
      packages=['components', 'gui'],
      package_dir={"": "src"},
      scripts=["bin/main.py"],
      )
