try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    "description": "Unofficial Google Play Music player",
    "author": "Michal Odnous",
    "url": "https://github.com/odiroot/PyGPMP",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["gpmp"],
    "scripts": [],
    "name": "PyGPMP",
}

setup(**config)