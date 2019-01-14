#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'jinja2',
    'pyrobuf>=0.8.5',
    'schematics',
]


setup(
    author="Almog Cohen",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Convert ProtoBuf proto file to cute Schematics classes file",
    entry_points={
        'console_scripts': [
            'protobuf_schematics=protobuf_schematics.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='protobuf_schematics',
    name='protobuf_schematics',
    packages=find_packages(include=['protobuf_schematics']),
    test_suite='tests',
    url='https://github.com/AlmogCohen/protobuf-schematics',
    version='0.2.0',
    zip_safe=False,
)
