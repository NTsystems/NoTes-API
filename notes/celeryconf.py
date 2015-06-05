from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

# nisam sigurna za putanju...
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")

app = Celery('notes.apps.account')

CELERY_TIMEZONE = 'UTC'

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
	print 'Request: {0!r}'.format(self.request)