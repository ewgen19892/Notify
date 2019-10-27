"""Celery app."""
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notify.settings")

app: Celery = Celery("Notify")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
