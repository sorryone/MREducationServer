# -*- coding: utf-8 -*-
__author__ = 'maxijie'

from lib.djhelper.api_view import api_view, api_result


@api_view(["GET"])
@api_result
def Test(request):
    if request.method == "GET":
        print("This is Test")
        return 0, {"value": "This is Test"}
