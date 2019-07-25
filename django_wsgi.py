#!/usr/bin/env python
# coding: utf-8

from django.core.wsgi import get_wsgi_application
import os
import sys
import importlib

importlib.reload(sys)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MREducationServer.settings")
application = get_wsgi_application()
