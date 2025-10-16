import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_shopping_site.settings")
app = Celery("online_shopping_site")
app.config_from_object("django.config:settings", namespace="CELERY")
app.autodiscover_tasks()
