# https://packaging.python.org/tutorials/packaging-projects/

# python setup.py sdist bdist_wheel

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gameoflife_zvolsky",
    version="0.0.2",
    author="Mirek Zvolský",
    author_email="zvolsky@seznam.cz",
    description="game of life",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zvolsky/game-of-life",
    py_modules=("gameoflife",), 
    entry_points = {'console_scripts': ['game-of-life=gameoflife:from_stdin']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
