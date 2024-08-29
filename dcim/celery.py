import django
import os

from celery.schedules import crontab
from celery import Celery

from datetime import timedelta, datetime
from django.conf import settings
import json
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcim.settings')

logger = logging.getLogger(__name__)

app = Celery('dcim')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

