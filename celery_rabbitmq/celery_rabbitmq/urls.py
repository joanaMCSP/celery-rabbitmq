from django.conf.urls import url, include
from rest_framework import routers
from celery_rabbitmq import views


router = routers.DefaultRouter()

router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
