# tourn-handler-app
[![Build Status](https://travis-ci.com/peertosir/tourn-handler-app.svg?branch=main)](https://travis-ci.com/peertosir/tourn-handler-app)

API for handling tournaments in any kind of sports written in Python with Travis CI and Docker

## Requirements

- Docker installed

- Python installed(OPTIONAL)

- IDE(VSCode, PyCharm, Atom, etc.)

## Commands

`docker-compose run --rm app sh -c "python manage.py makemigrations"` - make migration

`docker-compose run --rm app sh -c "python manage.py test"` - run tests

`docker-compose run --rm app sh -c "python manage.py test && flake8"` - run tests and linting

`docker-compose run --rm app sh -c "python manage.py startapp <app_name>"` - make new app, where _**<app_name>**_ = name of application

`docker-compose run --rm app sh -c "python manage.py migrate"` - apply migrations to docker db





## FAQ

#### Command doesn't work in docker
Try to clear docker cache and rerun command

Clear docker build cache:
`docker builder prune`