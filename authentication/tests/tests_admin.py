# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present 
"""

from django.test import (TestCase,
                         Client)
from django.contrib.auth import get_user_model 
from django.urls import reverse


class AdminSiteTests(TestCase):

  def setUp(self):
    self.client = Client()
    self.admin_user = get_user_model().objects.create_superuser(
          email = 'admin@cbdemos.com',
          password = 'admin'
    )
    self.client.force_login(self.admin_user)
    self.user = get_user_model().objects.create_user(
                  email = 'test@cbdemos.com',
                  password = 'tester123',
                  name = 'test.user'
    )

  def test_users_listed(self):
    url = reverse('admin:core_user_change_list')
    res = self.client.get(url)
    
    self.assertContains(res, self.name)
    self.assertContains(res, self.email)
  
  def test_user_change_page(self):
    """Test that the user edit page works"""
    # this may need to change to 'authentication:core_user_change'
    url = reverse('admin:core_user_change', args=[self.user.id])
    res = self.client.get(url)
    
    self.assertEqual(res.status_code, 200)
    