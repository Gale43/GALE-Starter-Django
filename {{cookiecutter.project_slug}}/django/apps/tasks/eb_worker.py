{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

#
# ElasticBeanstalk worker support
# in addition to calling all the tasks from this entry point,
# you need to create and plug an SQS queue to the EB environment
#

from django.http import HttpResponse, Http404

from . import task1

def index(payload):
    # if the queue type isn't SQS we fail
    if settings.QUEUE_TYPE != 'sqs':
        return Http404("Host configuration does not authorize this endpoint.")


    # switch on the payload action_type, verify payload, extract parameters
    # and call the tasks

    # this sample is calling a single task
    task1(payload.param1)

    return HttpResponse("OK")


{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif %}
