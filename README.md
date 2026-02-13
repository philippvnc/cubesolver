# Cube Solver

This project contains code for a lego mindstorms rubiks cube solver robot.<br>
Its written in python using the [pybricks](https://docs.pybricks.com/en/latest/index.html) module.

## Getting started

Make sure you have a python 3.13 installation on your system.<br>
Then follow these steps.

### Create virtual environment
```shell
python -m venv .venv
```

### Activate virtual environment
```shell
source venv/bin/activate  # macOS/Linux
```

### Install dependencies
```shell
pip install -r requirements.txt
```

### Run tests
```shell
python -m unittest discover
```

### Build and execute on robot
```shell
python build.py
```

### Open tasks

- improve solution generation speed
- add solution generation progress feedback
- improve scan speed
- improve solution execution effectiveness
- refactor for less code duplication and magic numbers
- improve testing setup (run all tests)
- add typehints everywhere
- remove debugging prints
- add building instructions

