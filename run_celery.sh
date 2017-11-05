#!/bin/sh

sleep 10

cd celery_rabbitmq

su -m myuser -c "celery worker -A celery_rabbitmq.celeryconf -Q default -n default@%h"
