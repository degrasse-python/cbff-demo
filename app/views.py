# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021
"""
import os
# for api requests
import json

from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render, 
                              get_object_or_404, 
                              redirect)
from django.template import loader
from django.http import (HttpResponse,
                        JsonResponse)
from django.core import serializers
import pymongo

from app.models.models import Orders
from app.models.mongo_models import MongoOrders
from app.utils import *
from core.flags import Flags

FLAGS = Flags()

@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'
    context['enableSocialSignOn'] = FLAGS.enableSocialSignOn
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))




@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url and load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        ### --- Feature FLAGS --- ###
        # add ff inside context dict to pass them to the templates on frontend
        context['enableCustomersKPI'] = FLAGS.enableCustomersKPI.is_enabled()
        context['LineGraphVariant'] = FLAGS.LineGraphVariant.get_value()
        context['enableLineGraph'] = FLAGS.enableLineGraph.is_enabled()
        context['enableRevenueKPI'] = FLAGS.enableRevenueKPI.is_enabled()
        context['enableNewTaskButton'] = FLAGS.enableNewTaskButton.is_enabled()

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        print('Random 500 errors')
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))



def pivot_data(request):
    dataset = Orders.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)



# return data from api
def getCsvData(path='./data.csv', secret=None, key=None):
    # getdata = db.get_ecomm_data() # create function to get data
    if os.path.exists('./data.json'):
        return json.dumps('./data.json')

    else:
        Csv2Json(path, './data.json')
        return json.dumps('./data.json')
        
        
        #return json.dumps(getdata)

# return data from api
def line_chart(request):
    ecomm_data = {}
    amt = []
    dates = []
    price = []
    country = []

    # example of all data selected by date of today? 
    """
    data = MongoOrders.objects.all() \
        .extra(select={'InvoiceDate': connections[MongoOrders.objects.db].ops.date_trunc_sql('InvoiceDate', 'date')}) \
        .values('InvoiceDate') 
    """

    querysetall = MongoOrders.objects.all()

    return JsonResponse(list(querysetall), safe=False)

# return data from api
def get_data(request):
    import pandas as pd
    # path
    data = "./data.csv"
    # dataframe from data
    df = pd.read_csv(data, encoding="ascii", encoding_errors="replace")
    # json
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    json.dumps(parsed, indent=2)

    return JsonResponse(json.dumps(parsed, indent=2), safe=False)
    
        
        

