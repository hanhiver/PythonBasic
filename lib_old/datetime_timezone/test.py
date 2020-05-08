# Make sure that the library about datetime that you write will include the 
# TIMEZONE information. 

import datetime
import pytz
import iso8601

def utcnow():
    """
    the function that return datetime with timezone information. 
    """
    return datetime.datetime.now(tz=pytz.utc)

print("utcnow(): ", utcnow())
print("utcnow().isoformat(): ", utcnow().isoformat())

print("iso8601 format: ", iso8601.parse_date(utcnow().isoformat()))

