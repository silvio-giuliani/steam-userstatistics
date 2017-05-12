# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='steam-userstatistics',
    version='0.1.0',
    description='Displays steam user game data usage',
    long_description=readme,
    author='Silvio Giuliani',
    author_email='silvio.giuliani@gmail.com',
    url='https://github.com/silvio-giuliani/steam-userstatistics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

