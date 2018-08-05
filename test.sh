psql -c 'create database mydb'

pipenv run python3 manage.py migrate
pipenv run pytest

psql -c 'drop database mydb'