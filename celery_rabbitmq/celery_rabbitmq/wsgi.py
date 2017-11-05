import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_rabbitmq.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
