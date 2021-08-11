# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

class UserAdmin(UserAdmin):
  ordering = ['id']
  list_display = ['email', 'name']
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (('Personal Info'), 
        {'fields': ('name',)}),
      (('Permissions'), 
        { 'fields': ('is_active', 'is_staff', 'is_superuser',)}),
      (('Important Dates'),
        {'fields': ('last_login',)})
  )

admin.site.register(models.User, UserAdmin)

