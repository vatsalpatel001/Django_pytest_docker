# Python Django Docker Application with Pytest and Coverage

[![Docker Pulls](https://img.shields.io/docker/pulls/python012/python_django_pytest_docker)](https://hub.docker.com/r/python012/python_django_pytest_docker)

This repository contains a Dockerized Python Django application with Pytest for testing and coverage reporting. You can easily run the application in a container and perform testing and coverage analysis.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Directory Structure](#directory-structure)
- [Running Tests and Coverage](#running-tests-and-coverage)
- [Docker Image](#docker-image)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system.

## Quick Start

1. **Pull the Docker Image**:

   To get started, pull the Docker image from Docker Hub:

   ```bash
   docker pull python012/python_django_pytest_docker:tagname
   
## Run the Docker Container:

- Start a Docker container with the Django application:

```docker run -p 8000:8000 python012/python_django_pytest_docker:tagname

- The Django application will be accessible at [http://localhost:8000]

## Directory Structure

src/: Contains the Django application source code.
requirements.txt: Lists the Python dependencies.
Dockerfile: Defines the Docker image configuration.
run.sh: Script for running tests, coverage, and the Django application.


## Running Tests and Coverage
The run.sh script in the project root simplifies running tests and generating coverage reports. Here's what it does:

Runs your tests with coverage using coverage run.
Generates a coverage report in HTML format using coverage html.
Runs Pytest for additional testing.
Starts your Django application with python manage.py runserver.
To execute these steps, run the following command within your Docker container:

/bin/bash /app/run.sh
The coverage report will be available in the htmlcov directory.

Docker Image
You can build your own Docker image based on the provided Dockerfile or use the pre-built image from Docker Hub:

Docker Hub Reposiory: python012/python_django_pytest_dockert

Contributing
Contributions are welcome! Please read our contribution guidelines for more information.

License
This project is licensed under the MIT License - see the LICENSE file for details.

