from __future__ import absolute_import
import os
from celery import Celery


# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('steelkiwi_python_test_task')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
