from setuptools import setup, find_packages

setup(
    name = "DungeonGame",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
)