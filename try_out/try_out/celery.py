import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try_out.settings')

app = Celery('try_out')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request}')
