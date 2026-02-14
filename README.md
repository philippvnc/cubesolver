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
python -m unittest discover -v -b
```

### Build and execute on robot
```shell
python build.py
```

### Open tasks

- add solution generation progress feedback
- improve scan speed
- improve solution execution effectiveness
- add typehints everywhere
- replace debugging prints with logging
- add building instructions

