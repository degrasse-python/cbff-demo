import csv
import json
import datetime

from django.db import models

# format of the datetime str in the row on the dt col
FORMAT = "%m/%d/%Y %H:%M"

class FormattedDateTimeField(models.DateTimeField):
  def value_to_string(self, obj):
    dt_string = self.value_from_object(obj)
    if dt_string:
      # return the datetime str as a formatted dt obj
      return datetime.datetime.strptime(dt_string, FORMAT)
    return ''

# TODO create functions to connect to backend and get data
class BackendConnection:
  def __init__(self, secret=None, key=None) -> None:
    self.secret = ''
    self.key = ''
    pass

class Csv2Json:
  """
  Create a json file using an existing csv file
  
  csv_path: existing csv
  json_path: path to where you want to save the new json

  """
  def __init__(self, csv_path, json_path) -> None:
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
