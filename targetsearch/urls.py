#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.urls import path, re_path
from .views import *

urlpatterns = [
        path('', newTS, name='newTS'),
        path('drugIndTable', drugIndTable, name='drugIndTable'),
        path('compoundNames/<query>', compoundNames, name='compoundNames'),
        path('targetNames/<query>', targetNames, name='targetNames'),
        path('ajax/<action>', ajax, name='targetsearch-ajax'),
        path('detail/<id>', detailPage),
        ]
