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
    path('', views.pages, name='pages'
    ),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    # API paths
    path('get_data', views.get_data, name='get_data'),

    # load data 
    path('pivot_data', views.pivot_data, name='pivot_data'),

    # graphs
    path('line_chart', views.line_chart, name='line_chart'),

]
