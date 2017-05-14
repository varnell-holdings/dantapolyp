"""setup for dantapolyp project."""

from setuptools import setup

setup(
    name='dantapolyp',
    version='0.1',
    license='MIT',
    packages=['patfind'],
    install_requires=['fuzzyfinder'],
    author='J Tillett',
    author_email='tillett1957@gmail.com',
    include_package_data=True,
    package_data={
        'patfind': ['danta_study.csv'],
    },
    entry_points={
        'console_scripts': [
            'patfind = patfind.dantafind:main'
            ]
    })
