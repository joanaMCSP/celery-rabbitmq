import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_rabbitmq.settings")

app = Celery('celery_rabbitmq')

CELERY_TIMEZONE = 'UTC'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
