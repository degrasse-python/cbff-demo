import csv
import json
import datetime

from django.db import models
from django.db.models import Sum, Avg, Min, Max
from app.models.mongo_models import *

import pymongo
from pymongo import MongoClient
from plotly.offline import plot
from plotly.graph_objs import Scatter

# format of the datetime str in the row on the dt col
FORMAT = "%m/%d/%Y %H:%M"

class FormattedDateTimeField(models.DateTimeField):
  def value_to_string(self, obj):
    dt_string = self.value_from_object(obj)
    if dt_string:
      # return the datetime str as a formatted dt obj
      return datetime.datetime.strptime(dt_string, FORMAT)
    else:
      print("no obj to parse with datetime from file")

# TODO create functions to connect to backend and get data
class BackendConnection:
  def __init__(self, secret=None, key=None):
    self.secret = ''
    self.key = ''
    pass
  
    def get_db_handle(db_name, host, port, username, password):
      """
        Setup connection to database
        
      """
      client = MongoClient(host=host,
                          port=int(port),
                          username=username,
                          password=password
                        )
      db_handle = client['db_name']
      return db_handle, client
    
    def upload_csv_to_mongodb(data, db_name, col_name, connect_string=None):
      """ 
        Upload CSV data to database

        data: csv file
        connect_string: proper connection string to access mongodb instance
        db_name:  name of new/existing db
        col_name: name of new/existing collection (table) in the db

        data will be converted then inserted as a list of dict's which only contain 
        col and values, no row number info

      """
      import pandas as pd
      # connect to instance
      # connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 
      # db-admin:ishqQNfeHvDf4OED
      # "mongodb+srv://db-admin:ishqQNfeHvDf4OED@cluster007.c5d1k.mongodb.net/opensourceEcomm?retryWrites=true"
      # 'opensourceEcomm' 'ecomm1'
      if connect_string is None:
        connect_string = "mongodb+srv://db-admin:ishqQNfeHvDf4OED@cluster007.c5d1k.mongodb.net/opensourceEcomm?retryWrites=true"
        # connect to the mongodb instance
        my_client = pymongo.MongoClient(connect_string)
      
      else:
        my_client = pymongo.MongoClient(connect_string)
      
      # First define the database name
      dbname = my_client[db_name]

      # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
      collection_name = dbname[col_name]

      # use pandas to upload data and turn it into a dict for the db
      df = pd.read_csv(data, encoding="ascii", encoding_errors="replace")
      df_dict = df.to_dict('records')
      # insert all data into db collect : list of dict's
      collection_name.insert_many(df_dict)
      # Check the count
      count = collection_name.count()
      print(count)
      print("Finished uploading csv to db")



class Csv2Json:
  """
  Create a json file using an existing csv file
  
  csv_path: existing csv
  json_path: path to where you want to save the new json

  """
  def __init__(self, csv_path, json_path) -> dict:
    self.csv_path = csv_path
    self.json_path = json_path


    # Function to convert a CSV to JSON
    # Takes the file paths as arguments
    def csv_to_dict(csvFilePath):
      """Create a dictionary from a CSV"""
      # create a dictionary
      data = {}
      
      # Open a csv reader called DictReader
      with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
          
          # Assuming a column named 'No' to
          # be the primary key
          key = rows['No']
          data[key] = rows

      # Open a json writer, and use the json.dumps()
      # function to dump data
      return data

    def csvdict_to_json(jsonFilePath, data=None):
      """ Create a json from a csv dict """
      with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    csvdict_to_json(self.json_path, data=csv_to_dict(self.csv_path))


# return data from api
def lineplot(path=None):
    import pandas as pd
    
    # path
    if path == None:
      path = "./data.csv"
    # dataframe from data
    df = pd.read_csv(path, encoding="ascii", encoding_errors="replace")
    # json
    # df['InvoiceDate'] = df['InvoiceDate'].dt.strftime('%m-%d%Y')
    df.InvoiceDate = pd.to_datetime(df.InvoiceDate)
    df['InvoiceDate'] = df['InvoiceDate'].dt.date
    g = df.groupby('InvoiceDate')
    y_data = g.UnitPrice.agg(sum).array
    x_data = g.InvoiceDate.unique().array
    new_x = []
    for i in x_data:
      new_x.append(i[0])
    # import plotly.express as px
    # fig = px.line(df, x="x", y="y", title="Unsorted Input") 
    # fig.show()
    
    return new_x, y_data

def query():
  queryset_date = MongoOrders.objects.filter().values('InvoiceDate')
  queryset_price = MongoOrders.objects.filter().values('UnitPrice')