# coding: utf-8

from django.conf.urls.defaults import patterns, include, url
import os
from django.conf import settings
from about_django.views import GetBody

urlpatterns = patterns('',
    url(r'^$', 'about_django.views.index'),
    url(r'^body$', GetBody.as_view()),
    url(r'^getbody/$', 'about_django.views.get_body'),
    (r'^site_static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)
