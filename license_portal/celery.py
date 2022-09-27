from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'license_portal.settings')
app = Celery('license_portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



# app.conf.beat_schedule = {
# 'email_send_minute': {
# 'task': 'email_sending',
# 'schedule': 60.0}
# }

app.conf.beat_schedule = {
'email_send': {
'task': 'email_sending',
'schedule': crontab(minute=0, hour=5)}
}