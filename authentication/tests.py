# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present 
"""

from django.test import (TestCase,
                         Client)
from .views import *
from .forms import *


class SetUp_Class(TestCase):

  def setUp(self):
    self.user = User.objects.create(email="user@mp.com", password="user", first_name="user", phone=12345678)

### --- Testing the Forms --- ###
# Login Form
class Login_Form_Test(TestCase):

  # Valid Form Data
  def test_LoginForm_valid(self):
    form = LoginForm(data={'username': "test@mp.com", 'password': "user", 'first_name': "user", 'phone': 12345678})
    self.assertTrue(form.is_valid())

  # Invalid Form Data
  def test_LoginForm_invalid(self):
    form = LoginForm(data={'Username': "", 'Password': "mp", 'first_name': "mp", 'phone': ""})
    self.assertFalse(form.is_valid())

# Sign Up Form
class Sign_Up_Form_Test(TestCase):
  # Valid Form Data
  def test_SignUpForm_valid(self):
    form = SignUpForm(data={'Username': "test@mp.com",
                            'Email': "user", 
                            'Password': "user", 
                            'Password check': "user", 
                            'phone': 12345678})
    self.assertTrue(form.is_valid())

  # Invalid Form Data
  def test_SignUpForm_invalid(self):
    form = SignUpForm(data={'Username': "test@mp.com",
                              'Email': "user", 
                              'Password': "user", 
                              'Password check': "user", 
                              'phone': 12345678})
    self.assertFalse(form.is_valid())


### --- Testing the Views --- ###
# TODO check all the views for the testing
class User_Views_Test(SetUp_Class):

  # Valid Data
  def test_login_view(self):
    user_login = self.client.login(email="user@mp.com", password="user")
    self.assertTrue(user_login)
    response = self.client.get("/")
    self.assertEqual(response.status_code, 302)

  # Valid Data
  def test_logout_view(self):
    response = self.client.get("include url for add user view")
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "include template name to render the response")

  # Invalid Data
  def test_register_user_invalidform_view(self):
    response = self.client.post("include url to post the data given", {'email': "admin@mp.com", 'password': "", 'first_name': "mp", 'phone': 12345678})
    self.assertTrue('"error": true' in response.content)

  # Valid Data
  def test_add_admin_form_view(self):
    user_count = User.objects.count()
    response = self.client.post("include url to post the data given", {'email': "user@mp.com", 'password': "user", 'first_name': "user"})
    self.assertEqual(response.status_code, 200)
    self.assertEqual(User.objects.count(), user_count+1)
    self.assertTrue('"error": false' in response.content)


