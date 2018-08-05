#!/bin/bash
set -euo pipefail

createdb -h localhost -p 5432 test
export DATABASE_URL=postgres://localhost:5432/test

pipenv run python3 manage.py migrate
pipenv run pytest

dropdb test