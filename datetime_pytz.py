import datetime
import pytz
 
# local = datetime.datetime.now()
# print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
 
 
tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.datetime.now(tz_NY)
print(datetime_NY)
# print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
 
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print(datetime_London)
# print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone()
datetime_London = datetime.datetime.now(tz_London)
print(datetime_London)