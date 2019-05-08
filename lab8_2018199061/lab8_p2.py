def removeValuesInPlace(L, threshold):
    """
    Removes all item in L that is bigger(>) than the threshold and returns L

    Parameters:
        L (list): list that will be mutated
        threshold (int or float): the threshold

    Returns:
        L (list): list that is mutated
    """
    L_copy = L[:]  # copy of list L

    for item in L_copy:
        if item > threshold:
            # delete item from the original list
            L.remove(item)
    return L
