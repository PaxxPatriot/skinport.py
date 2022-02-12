from setuptools import setup
import re

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("skinport/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("version is not set")

packages = [
    "skinport",
]

setup(
    name="skinport.py",
    author="PaxxPatriot",
    version=version,
    packages=packages,
    license="MIT",
    description="A Python wrapper for the Skinport API",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
