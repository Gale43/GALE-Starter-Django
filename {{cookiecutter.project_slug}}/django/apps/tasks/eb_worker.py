{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

#
# ElasticBeanstalk worker support
# in addition to calling all the tasks from this entry point,
# you need to create and plug an SQS queue to the EB environment
#
import logging
import json
import inspect

from django.conf import settings
from django.http import HttpResponse, Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

import apps
from . import QueueableTask

'''
    a sample task is in the apps.api folder
    we put it there, just to show that the tasks can be anywhere
    (but it doesn't really make sense for tasks to be in the api folder)

'''

def get_queueable_tasks():
    tasks = {}
    # inspect modules from the apps module
    for name, obj in inspect.getmembers(apps):
        if inspect.ismodule(obj):
            # keep only the QueueableTask sub-classes
            for class_name, c in inspect.getmembers(obj):
                # print("{} >>> {}".format(class_name, c))
                if inspect.isclass(c) and issubclass(c, QueueableTask):
                    try:
                        action = c().action_name()
                        print('task found: {} >>> {}'.format(class_name, c))
                        tasks[action] = c
                    except AttributeError:
                        # we ignore classes that don't have the action_name()
                        # mostly done for the LoyaltyClass itself
                        pass
    return tasks


@api_view(['POST'])
def index(request):
    if settings.QUEUE_TYPE != 'sqs':
        return Http404("Host configuration does not authorize this endpoint.")

    try:
        body = request.body.decode('utf-8')
        payload = json.loads(body)

        action = payload.get('action')
        tasks = get_queueable_tasks()

        # call the run
        try:
            task = tasks[action]()
            task.decode_args_and_run(payload)
        except KeyError:
            return Http404("Payload action does not exist.")
        else:
            return Http404("Payload action does not exist.")

    except Exception as e:
        return HttpResponse("KO")

    return HttpResponse("OK")
{% else %}
# If you are not using celery/tasks, you can remove this app
{% endif %}
