#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

VERSION = '0.0.1'
LONG_DESC = """\
"""

setup(name='django-base-image',
      version=VERSION,
      description="",
      long_description=LONG_DESC,
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='django, image placeholder, base64, png',
      author = 'Eric Lindstrom',
      author_email = 'eric.lindstrom@gmail.com',
      url='http://github.com/ericlindstrom/django-base-image',
      packages=find_packages(exclude=['tests']),
      include_package_data = True,
  )
