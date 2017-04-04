{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

from .task1 import queue_task1

{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif %}
