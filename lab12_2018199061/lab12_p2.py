def moderateDays(mydict):
    '''Returns a list [...] of the days for which the average
    temperature was between 70 and 79 degrees.
    '''
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    # return list of days whose temperature is between 70 and 79
    return [day for day in days if 70 <= mydict[day] <= 79]