# -*- coding: utf-8 -*-
__author__ = 'maxijie'

from django.http import HttpResponse
import json


def Test(request):
    print("This is Test")
    return HttpResponse(json.dumps({"valuse": "This is Test"}),
                        content_type='application/json')
