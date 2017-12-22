{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

class QueueableTask():
    pass

{% else %}
# If you are not using celery/tasks, you can remove this app
{% endif %}
