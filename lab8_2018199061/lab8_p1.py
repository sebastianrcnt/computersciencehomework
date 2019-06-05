def resetValuesInPlace(L, threshold):
    """
    Changes all item in L that is bigger(>) than the threshold to 0 and returns L

    Parameters:
        L (list): list that will be mutated
        threshold (int or float): the threshold

    Returns:
        L (list): list that is mutated
    """
    for i in range(len(L)):
        # if the ith item in L is under threshold, reassign its value to 0
        if L[i] > threshold:
            L[i] = 0
    # return the mutated list
    return L
