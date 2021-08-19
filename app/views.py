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

from .models import Orders
from .utils import Csv2Json
from core.flags import Flags


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'
    context['enableSocialSignOn'] = Flags.enableSocialSignOn
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url and load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        ### --- Feature Flags --- ###
        # add ff inside context dict to pass them to the templates on frontend
        # context['enableCustomersKPI'] = Flags.enableCustomersKPI
        context['LineGraphVariant'] = Flags.LineGraphVariant
        context['enableLineGraph'] = Flags.enableLineGraph
        context['enableRevenueKPI'] = Flags.enableRevenueKPI
        #context['enableNewTaskButton'] = Flags.enableNewTaskButton
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
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
def getEcommData(path='./data.csv', secret=None, key=None):
    # getdata = db.get_ecomm_data() # create function to get data
    pass
        
        
    #return json.dumps(getdata)