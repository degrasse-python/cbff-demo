# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021
"""

from django.contrib import admin
from django.urls import path, re_path
from app import views
from authentication.views import login_view


urlpatterns = [

    # The home page
    path('', login_view, name="login"),
    path('admin/', admin.site.urls, name='admin'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    # API paths
    path('api', views.getEcommData, name='getEcommData'),

    # load data 
    path('data', views.pivot_data, name='pivot_data'),

    # load csv
    path('CsvData', views.getCsvData, name='getCsvData'),


]
