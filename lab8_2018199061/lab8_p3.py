def resetValues(L, threshold):
    """
    Returns a new list that changes numbers that are bigger than the threshold to 0
    Parameters:
        L (list): list that will be checked
        threshold (int or float): the threshold

    Returns:
        Result (list): new list with numbers bigger than threshold is changed to 0
    """
    Result = []  # create new list variable
    for item in L:
        if item > threshold:  # if the item in L is bigger than threshold, 0 is appended to Result
            Result.append(0)
        else:  # otherwise the item in L is appended to Result
            Result.append(item)
    return Result  # Result is returned
