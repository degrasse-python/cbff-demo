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
from rox.server.rox_server import Rox

from app.models.models import Orders
from app.models.mongo_models import MongoOrders
from app.utils import *
from core.flags import Flags, ROLLOUT_ENV_KEY

flags = Flags()
  # Setup Feature Management SDK
try:
  flag_dict = {}
  # Register the flags container
  Rox.register('default-kpi', flags)
  print("Feature Management Flags Registered")
  # Setup the environment key
  cancel_event = Rox.setup(ROLLOUT_ENV_KEY, flags.options).result();
  print("Feature Management Setup - Starting Server")
  print("enableLineGraph: %s" % (flags.enableRevenueKPI.is_enabled()))
  print("enableRevenueKPI: %s" % (flags.LineGraphVariant.get_value()))
except Exception as e:
  print('%s (%s)' % (e, type(e)))

def index(request):
    context = {}
    context['segment'] = 'index'
    context['enableSocialSignOn'] = Flags.enableSocialSignOn
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def pages(request):
  
  context = {}
  # All resource paths end in .html.
  # Pick out the html file name from the url and load that template.
  # flags = Flags()
  try:
    Rox.fetch()
    print('fetched')
  except Exception as e:
    print('%s (%s)' % (e, type(e)))
  try:
    #load_template = request.path.split('/')[-1]
    #context['segment'] = load_template
    context['segment'] = 'dashboard'
    html_template = loader.get_template( 'dashboard.html' )
    ### --- Feature FLAGS --- ###
    ##Rox.fetch()
    # add ff inside context dict to pass them to the templates on frontend
    context['enableCustomersKPI'] = flags.enableCustomersKPI.get_value()
    context['LineGraphVariant'] = flags.LineGraphVariant.get_value()
    context['enableLineGraph'] = flags.enableLineGraph.is_enabled()
    context['enableRevenueKPI'] = flags.enableRevenueKPI.is_enabled()
    # context['enableNewTaskButton'] = flags.enableNewTaskButton.get_value()
    print("enableLineGraph: %s" % (context['enableLineGraph']))
    print("enableRevenueKPI: %s" % (context['enableRevenueKPI']))
    print("LineGraphVariant: %s" % (context['LineGraphVariant']))
    
    x_data, y_data  = lineplot(path="./app/data.csv")
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
                        show_link=False, link_text="",
                        output_type='div', include_plotlyjs=False,
                        )

    context['LineGraphPlotly'] = plot_div
    print("plot_finished")
    # html_template = loader.get_template( load_template )
    return HttpResponse(html_template.render(context, request))
        
  except template.TemplateDoesNotExist:
      html_template = loader.get_template( 'page-404.html' )
      return HttpResponse(html_template.render(context, request))

  except Exception as e:
    print('%s (%s)' % (e, type(e)))
    html_template = loader.get_template( 'page-500.html' )
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
    
        
        

