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

