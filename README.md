# User Manager

## Description
This repo contains service that is built with Django.
This service can be used by another service to provide user management-related functionality, such as:
- Managing resources:
    - User (CRUD)
    - Permission (CRUD)
    - Role (CRUD)

## How to run
### Docker
You can run user manager itselfs by:
- Install docker
- Build and run docker image as below
```shell script
$ docker build -t user-manager .
$ docker run \
      -p 8000:8000 \
      --env-file .env \
      user-manager runserver 0.0.0.0:8000
```
or you can run user-manager with all needed stack by:
- Install docker
- Run user-manager, PostgreSQL, PostgREST and adminer
```shell script
$ docker-compose up
```
