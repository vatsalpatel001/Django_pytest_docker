#!/bin/bash

# Run your tests with coverage
coverage run --source='.' --rcfile=.coveragerc manage.py test

# Generate the coverage report in HTML format
coverage html

# Run pytest
pytest

# Start your Django application
python manage.py runserver 0.0.0.0:8000
