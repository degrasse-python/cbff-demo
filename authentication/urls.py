# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021

"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    #path("logout/", LogoutView.as_view(), name="logout"),
    # for some reason the og one was not working
    path("logout/", login_view, name="logout")
]
