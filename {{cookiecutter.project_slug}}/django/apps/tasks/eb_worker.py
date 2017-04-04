{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

#
# ElasticBeanstalk worker support
# in addition to calling all the tasks from this entry point,
# you need to create and plug an SQS queue to the EB environment
#

from django.http import HttpResponse

from . import task1

def index(request):
    # switch on the payload action_type and call the tasks

    # this sample is calling a single task
    task1(request)


    return HttpResponse("OK")


{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif -%}
