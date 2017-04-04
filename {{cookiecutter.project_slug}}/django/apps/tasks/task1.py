{% if cookiecutter.use_tasks == 'y' %}
def task1(request):
    print('Request: {0!r}'.format(request))  # pragma: no cover



{% else %}
# Use this as a starting point for your project with celery/tasks.
# If you are not using celery/tasks, you can remove this app
{% endif -%}
