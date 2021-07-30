### Tests and linter status:
[![task-manager-check](https://github.com/RamiGaggi/python-project-lvl4/actions/workflows/task-manager-check.yml/badge.svg)](https://github.com/RamiGaggi/python-project-lvl4/actions/workflows/task-manager-check.yml)
### Codeclimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/6693f32bb699eefcafd1/maintainability)](https://codeclimate.com/github/RamiGaggi/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6693f32bb699eefcafd1/test_coverage)](https://codeclimate.com/github/RamiGaggi/python-project-lvl4/test_coverage)

This app can be found at https://task-manager-1085.herokuapp.com/

## Prerequisites
 - make
 - poetry

## Install
1) Clone repository ```git clone https://github.com/RamiGaggi/edu-task-manager.git```
2) Go to working directory ```cd edu-task-manager```
3) Install dependencies ```make install```
4) Set up environment variables in  *.env*
   - DB_ENGINE (defaults to SQLite), set another db engine this way, for example postgres `postgres://user:password@host:port/db_name`
   - SECRET_KEY, for generation you can use `make secret-key`

5) Сomplete setup `make setup`

## Run development server
```
make runserver
```
