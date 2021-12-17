# Multiprocessing-based pubsub implementation


[![Build Status](https://travis-ci.org/jflbr/multiprocessing-pubsub .svg?branch=master)](https://travis-ci.org/jflbr/multiprocessing-pubsub )
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Use case

Your task is to build an python application where a couple of processes communicate with each other using the publish-subscribe messaging pattern to exchange
objects.
## Application features

A publisher MotionDetector publishing the topic `MotionVector`, a
subscriber-publisher `SingleShotDetector` that consumes the `MotionVector`
topic and outputs messages in the `DetectionVector` topic, and, finally, a subscriber `Logger` that consumes objects from both the `MotionVector` and the
`DetectionVector` topics and logs them to standard output.
Here are examples of the properties that
messages could have:
### MotionVector:
* Timestamp
* Frame ID
* Bounding box (x, y, width, height) of a part of the image
where motion is detected
* Velocity vector (2d vector, with speed and direction)
### DetectionVector:
* Timestamp
* Frame ID
* Bounding box of the detected object
* Class prediction vector (example: car 98%, bike 5%)


## Working in the development environment
Short explanation:
```bash
pipenv sync --dev
pipenv shell
invoke compose-up
invoke test
```

```bash
pipenv sync --dev
```

### Entering a python virtual environment
```bash
pipenv shell
```

## Service tooling (built-in entrypoints)
Some built-in commands are provided thanks to the [`cookiecutter-aiohttp`](https://gitlab.aldebaran.com/kumoqi/tools/cookiecutter-aiohttp)
and [`invoke`](http://www.pyinvoke.org/). They provide an entrypoint that can
be called to perform common tasks usually run by the developper or the
continous integration system.

Each built-in entrypoint can be called either from inside or outside the virtual environment.

### Calling an entrypoint from outside your virtualenv
```bash
pipenv run invoke <entrypoint>
```

### Calling an entrypoint from inside your virtualenv
```bash
invoke <entrypoint>
```

You may also use the longer version (might be useful if it's in your command history):
```bash
pipenv run invoke <entrypoint>
```

### Calling multiple entrypoints all at once
You can chain call entrypoints, which is an `invoke` feature:

Example:
```bash
invoke format lint
```

This will call in order the `format` and the `lint` entrypoints. However, if
an entrypoint returns an error, the remaining ones will not be run.

### List of available entrypoints

- Code formatting

You can format all the code by calling:

```bash
invoke format
```

or check if it's already well formatted:

```bash
invoke check-format
```

- Code linting
  
You can run linters to perform some static analysis of your code by running:
```bash
invoke lint
```

- Run all the tests and record code coverage

```bash
invoke test
```

- Generate the coverage html report

```bash
invoke coverage
```

- Run the application

```bash
ivoke motion_detection
```

## Execute the tests
Following explains how to run the automated tests of the application.

### Run unit tests

Inside a virtualenv (`pipenv shell`), run:

```bash
# with the coverage report
pytest --cov=motion_detection tests/

# without the coverage
pytest tests/

# specific test module
pytest tests/devices/test_singleshot_detector.py

# specific test case
pytest tests/devices/test_singleshot_detector.py::test_put_message_type
```
