from copy import deepcopy
def addDailyTemp(mydict, day, temperature):
    '''
    Add key 'day' and value 'temperature' to the dictionary 'mydict'
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned.

    :param mydict: dictionary(key = day, value = temperature)
    :param day: date
    :param temperature: temperature
    :return: updated dictionary
    '''
    # make a (deep)copy of the dictionary
    updated_dict = deepcopy(mydict)
    # check whether parameter day is in keys of mydict
    # if day doesn't exist in mydict keys,
    if day not in mydict.keys():
        updated_dict[day] = temperature
    # if day already exist in mydict keys, do nothing
    # return updated dictionary
    return updated_dict