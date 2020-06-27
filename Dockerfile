FROM python:3.8.2-alpine3.11

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app/
WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
