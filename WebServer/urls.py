# -*- coding: utf-8 -*-
from django.urls import include, path
from WebServer.views import views
__author__ = 'maxijie'

urlpatterns = [
    path("test/", views.Test)
]
