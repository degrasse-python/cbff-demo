# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021
"""

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        BaseUserManager, 
                                        PermissionsMixin)


class UserManager(BaseUserManager):


  def create_user(self, username, email=None, password=None, **extra_fields):
    """Creates and saves new user"""
    if not email:
      raise ValueError('Users must have an email address')
    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password, **extra_fields):
    """ Creates amd saves a new superuser """
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
  """Custom User model that supports more attrs than base django user Class"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email'

