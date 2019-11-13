# Time module

import time

# Epoch seconds -> Seconds since 1/1/1970
epochseconds = time.time()
print(epochseconds)

# Current datetime
datetime = time.ctime(epochseconds)
print(datetime)

# Datetime module -> more easy

import datetime

today = datetime.datetime.today()
print(today)

# Get day, month, year, hour...
print('Current date: {}/{}/{}'.format(today.day, today.month, today.year))
print('Current time: {}:{}:{}'.format(today.hour, today.minute, today.second))