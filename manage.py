#!/usr/bin/env python
"""
Copyright (c) 2021
"""

import os
import sys
import csv

from app.models import Orders

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
    """
    path =  "./app/data/" # Set path of directory with data here
    os.chdir(path) # changes the directory
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Orders(InvoiceNo=row['InvoiceNo'], 
                        StockCode=row['StockCode'], 
                        Description=row['Description'], 
                        Quantity=row['Quantity'], 
                        # InvoiceDate=row['InvoiceDate'],
                        UnitPrice=row['UnitPrice'],
                        CustomerID=row['CustomerID'],
                        Country=row['Country'],)
            p.save()
    """

