# -*- coding: utf-8 -*-
from django.urls import path
from WebServer.views import views
from WebServer.views import login
from WebServer.views import manage
__author__ = 'maxijie'

urlpatterns = [
    path("test/", views.Test),
    path("checkVer/", login.checkVer),
    path("login/", login.userlogin),
    path("enter/", login.questionList),

    path("manage/index", manage.index),
    path("manage/login", manage.login),
    path("manage/school", manage.school),
    path("manage/question", manage.question),
    path("manage/manageUser", manage.manageUser),
    path("manage/chapter", manage.chapter),
    path("manage/course", manage.coursedesc),
    path("manage/selectSchool", manage.selectSchool),
    path("manage/uploadUser", manage.uploadUser),
]
