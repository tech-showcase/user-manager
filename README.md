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
- Install docker
- Build and run docker image as below
```shell script
$ docker build -t user-manager .
$ docker run -p 8000:8000 user-manager
```