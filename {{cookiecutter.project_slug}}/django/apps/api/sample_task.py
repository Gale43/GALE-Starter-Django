{% if cookiecutter.use_tasks == 'y' %}
import logging
import json

from django.conf import settings
from celery import task

from apps.tasks import QueueableTask
from apps.tasks.utils import submit_to_sqs

logger = logging.getLogger(__name__)


# this function needs to be referenced in the module's __init__
# otherwise celery will not auto-discover it
@task
def run_sample_task(an_argument):
    SampleTask().run(an_argument)


class SampleTask(QueueableTask):

    celery_task_function = run_sample_task
    ACTION_NAME = 'sample'

    def __init__(self):
        pass

    @classmethod
    def action_name(cls):
        return cls.ACTION_NAME

    def run(self, an_argument):
        print("SampleTask.run({})".format(an_argument))

    def decode_args_and_run(self, payload):
        an_argument = payload.get('an_argument', None)
        self.run(an_argument)

    def queue(self, an_argument):
        if settings.QUEUE_TYPE == 'sqs':
            payload = {
                'action': self.ACTION_NAME, # mandatory, used to ID this task in eb_worker.py
                'an_argument': an_argument,
            }
            result = submit_to_sqs(json.dumps(payload))
            if not result:
                logger.warn('Failed to submit SQS message: task1')
        else:
            try:
                self.celery_task_function.delay(an_argument)
            except Exception as e:
                logger.error('Celery Error {}'.format(e))
{% else %}
# You are not using celery/tasks, you can remove this file
{% endif %}
