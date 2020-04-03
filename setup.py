#!/usr/bin/env python3
from setuptools import setup


setup(
    name='importsort',
    description='''Decent import sorting for python files.''',
    version='0.0.1',
    author='Craig de Stigter',
    author_email='craig@destigter.nz',
    url='http://github.com/craigds/importsort',
    packages=['importsort'],
    python_requires='>=3.6',
    install_requires=['bowler>=0.8', 'toml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    entry_points={'console_scripts': ['importsort = importsort:main']},
)
