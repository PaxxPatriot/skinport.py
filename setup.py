import re

from setuptools import setup

version = ""
with open("skinport/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

with open("README.md") as readme_file:
    long_description = readme_file.read()

packages = [
    "skinport",
]

setup(
    name="skinport.py",
    author="PaxxPatriot",
    author_email="skinport.py@gmail.com",
    url="https://github.com/PaxxPatriot/skinport.py",
    version=version,
    packages=packages,
    license="MIT",
    description="A Python wrapper for the Skinport API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "aiohttp",
        "python-socketio[asyncio_client]",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
