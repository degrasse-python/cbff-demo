# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021
"""

from django.db import models


class Orders(models.Model):
  """
    EcommerceData
  """
  InvoiceNo = models.PositiveIntegerField(("InvoiceNo"),)
  StockCode	= models.CharField(("StockCode"),max_length=12)	
  Description = models.CharField(("Description"), max_length=100)	
  Quantity = models.IntegerField(("Quantity"))
  # 12/1/2010 8:26  MM-DD-YYYY HH:MM
  InvoiceDate	= models.DateTimeField(("InvoiceDate"), auto_now=True)
  UnitPrice	= models.DecimalField(("UnitPrice"), max_digits=1000000, decimal_places=2)
  CustomerID = models.PositiveIntegerField(("CustomerID"))
  Country = models.CharField(("Country") ,max_length=100)

  class Meta:
          ordering = ('InvoiceNo',) # Should be a tuple


