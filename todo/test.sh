#!/bin/bash
# Ubuntu

# Run test
mkdir -p coverage
coverage run --source='.' --data-file=./coverage/.coverage manage.py test
# Raise error if failed

# Generate report
coverage html -d ./coverage --data-file=./coverage/.coverage

# Generate coverage badge
cd coverage
coverage-badge -o ./coverage_badge.svg -f