#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name='raails',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'halo',
        'ipaddress',
        'requests',
        'rich',
        'shlex',
        'tldextract',
    ],
)
