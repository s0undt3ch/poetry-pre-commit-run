from __future__ import annotations

from setuptools import setup


setup(
    name="poetry-pre-commit-run",
    version="0.0.0",
    scripts=["poetry-wrapper"],
    install_requires=["poetry==1.7.1", "filelock"],
)
