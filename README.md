# Task Manager

Simple task management system. It allows you to set tasks with tags, assign performers and change their statuses.
This app can be found here: [Task Manager](https://task-manager-1085.herokuapp.com/)

## Tests and linter status

[![task-manager-check](https://github.com/RamiGaggi/python-project-lvl4/actions/workflows/task-manager-check.yml/badge.svg)](https://github.com/RamiGaggi/python-project-lvl4/actions/workflows/task-manager-check.yml)

## Codeclimate

[![Maintainability](https://api.codeclimate.com/v1/badges/6693f32bb699eefcafd1/maintainability)](https://codeclimate.com/github/RamiGaggi/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6693f32bb699eefcafd1/test_coverage)](https://codeclimate.com/github/RamiGaggi/python-project-lvl4/test_coverage)

## Prerequisites

- make
- poetry

## Install

1) Clone repository ```git clone https://github.com/RamiGaggi/edu-task-manager.git```
2) Go to working directory ```cd edu-task-manager```
3) Set up environment variables in  *.env*
   - DB_ENGINE (defaults to SQLite), set another db engine this way, for example postgres `postgres://user:password@host:port/db_name`
   - SECRET_KEY, for generation you can use `make secret-key`
4) Install dependencies ```make install``` or for Docker ```docker-compose build```
5) Сomplete setup `make setup` or for Docker ```docker-compose run --rm django make setup```

## Run development server

### Poetry

```
make runserver
```

### Docker

```
docker-compose up
```
