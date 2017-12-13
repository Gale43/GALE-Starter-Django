{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

#
# ElasticBeanstalk worker support
# in addition to calling all the tasks from this entry point,
# you need to create and plug an SQS queue to the EB environment
#
import logging
import json

from django.conf import settings
from django.http import HttpResponse, Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import task1

@api_view(['POST'])
def index(request):
    # if the queue type isn't SQS we fail
    if settings.QUEUE_TYPE != 'sqs':
        return Http404("Host configuration does not authorize this endpoint.")

    try:
        body = request.body.decode('utf-8')
        payload = json.loads(body)

        action = payload.get('action')

        param1 = payload.get('param1', None)

        # add reading all the parameters for all tasks here

        if action == 'task1':
            task1(param1)

        # one "elif action == 'bla':" per task

        else:
            return Http404("Payload action does not exist.")

    except Exception as e:
        return HttpResponse("KO")

    return HttpResponse("OK")


{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif %}
