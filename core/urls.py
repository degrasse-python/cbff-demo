# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
]
