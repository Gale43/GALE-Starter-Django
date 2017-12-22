{% if cookiecutter.use_tasks == 'y' %}
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from celery import Celery
from django.apps import apps, AppConfig
from django.conf import settings

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # pragma: no cover


app = Celery('project')


class CeleryConfig(AppConfig):
    name = 'apps.tasks'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

'''
    a sample task is in the apps.api folder
    we put it there, just to show that the tasks can be anywhere
    (but it doesn't really make sense for tasks to be in the api folder)

'''


{% else %}
# If you are not using celery, you can remove this app
{% endif %}
