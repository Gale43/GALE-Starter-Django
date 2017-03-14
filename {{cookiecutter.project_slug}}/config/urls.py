# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.defaults import (
    bad_request,
    server_error,
    page_not_found,
    permission_denied,
)

urlpatterns = [
    url(r'^400/$', bad_request, name="server_400"),
    url(r'^403/$', permission_denied, name="server_403"),
    url(r'^404/$', page_not_found, name="server_404"),
    url(r'^500/$', server_error, name="server_500"),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('apps.api.urls', namespace='project_api')),
]


if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
    from django.conf.urls.static import static
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
