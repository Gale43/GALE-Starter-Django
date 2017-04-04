{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-
import json

from django.conf import settings

logger = logging.getLogger(__name__)

def run_task1(request):
    print('Request: {0!r}'.format(request))  # pragma: no cover



def queue_task1(param1):
    if settings.QUEUE_TYPE == 'sqs':
        payload = {
            'action': 'task1',
            'param1': param1,
        }
        result = submit_to_sqs(json.dumps(payload))
        if not result:
            logger.warn('Failed to submit SQS message: task1')
    else:
        try:
            from .celery import task1
            task1.delay(param1)
        except Exception as e
            logger.error('Celery Error {}'.format(e))


{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif %}
