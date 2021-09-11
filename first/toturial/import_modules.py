import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
rads = math.radians(90)
#print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

# se i vilken directory du jobbar
print(os.getcwd())
print(os.__file__)
