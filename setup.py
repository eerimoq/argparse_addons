#!/usr/bin/env python

from setuptools import setup
import argparse_addons

setup(name='argparse_addons',
      version=argparse_addons.__version__,
      description=('Additional argparse types and actions.'),
      long_description=open('README.rst', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      keywords=['argparse'],
      url='https://github.com/eerimoq/argparse_addons',
      py_modules=['argparse_addons'],
      install_requires=[
      ],
      test_suite="tests")
