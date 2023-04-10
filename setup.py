#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='RAAILS',
    version='0.1.0',
    description='RAAAILS',
    author='Ultirian',
    author_email='my_email@example.com',
    packages=['RAAILS'],
    install_requires=[
        'halo',
        'ipaddress',
        'requests',
        'rich',
        'shlex',
        'tldextract',
    ],
)