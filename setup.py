#!/usr/bin/env python

from cuckoopy import __version__, __author__
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
        readme = f.read()

with open('LICENSE') as f:
        license = f.read()

setup(name='cuckoopy',
      version=__version__,
      description='Cuckoo Filter implementation in Python',
      long_description=readme,
      author=__author__,
      author_email='rajathagasthya@gmail.com',
      url='https://github.com/rajathagasthya/cuckoo-py',
      license=license,
      packages=find_packages(exclude=['tests']),
      install_requires=[],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7'
      ],
      extras_require={
          'test': ['pytest'],
      }
)