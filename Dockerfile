FROM python:3.8-alpine3.11

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pipenv install

COPY . /app/

ENTRYPOINT ["pipenv", "run", "python", "manage.py"]
