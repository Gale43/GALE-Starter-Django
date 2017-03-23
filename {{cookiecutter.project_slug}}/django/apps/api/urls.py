# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
from . import health

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^health$', health.health, name='health'),
]
