# -*- coding: utf-8 -*-
from django.http import HttpResponse

# this endpoint is called a regular intervals by monitoring apps to
# find out if all is well in the app

def health(request):
    # do health checks here
    return HttpResponse("OK")
