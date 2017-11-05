#!/bin/sh

#wait for Postgres to start
sleep 10

cd celery_rabbitmq

su -m myuser -c "python manage.py makemigrations celery_rabbitmq"

su -m myuser -c "python manage.py migrate"

su -m myuser -c "python manage.py runserver 0.0.0.0:8000"
