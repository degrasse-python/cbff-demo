# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present 
"""

# from typing_extensions import Required
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

def login_view(request):
    # TODO fix buggy logic with valid login
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            # get data from form
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # create user object
            user = authenticate(username=username, password=password)
            if user is not None:
                # if this works login the user and redirect user
                login(request, user)
                return redirect("/dashboard.html")
            else:    
                msg = 'Invalid credentials or user does not exist'    
        else:
            msg = 'Error validating the form'    
    else: 
        return render(request, "accounts/login.html")
    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def logout_view(request):
    
    msg = None
    if request.method == "POST":
        logout(request)
        return redirect("accounts/login.html")



def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


