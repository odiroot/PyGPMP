try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    "description": "Unofficial Google Play Music player",
    "author": "Michal Odnous",
    "url": "https://github.com/odiroot/PyGPMP",
    "version": "0.1",
    "license": "BSD",
    "install_requires": ["gmusicapi"],
    "packages": ["gpmp"],
    "scripts": [],
    "entry_points": {
        "console_scripts": ["pygpmp = gpmp.run:main"]
    },
    "name": "PyGPMP",
}

setup(**config)
