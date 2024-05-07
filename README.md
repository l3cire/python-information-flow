# The PIF Language

## Introduction
Welcome to PIF, short for Python Information Flow. PIF is an extension
of Python that adds support for information flow tracking 
to the Python language. This repository provides both a library of
custom secure types along with a transpiler that type checks PIF and 
transpiles into equivalent secure Python code.

## Setup

You will need to first install `conda` to manage the virtual environment
required to run the code. After installation and cloning this repository,
run the following command in the root directory

```bash
conda create --name pif python=3.9 -y
conda activate pif
```

You must also install `poetry` as a build backend and run in the root
directory
```bash 
peoetry install
```

To run the tests, make sure that `pytest` is installed in the virtual environment
and then you can simply execute the following command from
the root directory
```
pytest
```

This project does not exist yet as part of PYPI so it cannot be installed
with `pip`, but it is structured as a Python package to be added into a virtual
environment and used with your existing Python code.