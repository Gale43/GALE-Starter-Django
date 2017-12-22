{% if cookiecutter.use_tasks == 'y' %}
# these 2 declarations are necessary for celery auto-discovery and eb_worker.get_queueable_tasks()
# to find the tasks inside the module
from .sample_task import SampleTask, run_sample_task

{% else %}

{% endif %}
