"""setup for dantapolyp project."""

from setuptools import setup, find_packages

setup(
    name='dantapolyp',
    version='0.1',
    license='MIT',
    install_requires=['fuzzyfinder'],
    author='J Tillett',
    author_email='tillett1957@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': [
            'patfind = patfind.dantafind:main']}
        )
