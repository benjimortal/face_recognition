def hello_func(greeting, name ='You'):
    return f'{greeting}, {name}'

#print(hello_func())
#print(len(hello_func()))
#print(hello_func('hi', name = 'Jawid').title())


def student_info(*args, **kwargs):
    """print(args)"""
    #print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'jawid', 'age': 25}

#student_info('Math', 'Art', name='jawid', age=25)
student_info(*courses, **info)



# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # alla månader från januari till december

def is_leap(year):
    """Return True for leap years, False for non_leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(days_in_month(1999, 2))