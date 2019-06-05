line = 'hello world'
def countAllLetters(line):
    """
    Counts letters in 'line' and returns result list. If the line does not contain any letter, returns an empty list.

    Note 1: the list of letters must be sorted alphabetically.
    (This is a requirement in addition to the textbook problem.)
    Note 2: your letters in the result-list must be stored in lower-case. """

    # list to return
    result = []

    # list of alphabets
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # list of appearances(same length and index as list alphabets)
    appearances = [0] * len(alphabets)

    # for each lowered character in 'line', add 1 to the corresponding item in 'appearances'
    # appearances will contain the number of appearances of each alphabet in 'line'
    for char in line:
        if char.lower() in alphabets:
            appearances[alphabets.index(char.lower())] += 1

    # make tuple pairs of (alphabet, appearances) and append it to result(if it has 1 or more appearances)
    # since list alphabets is already sorted, the result will be also sorted in alphabetical order.
    for i in range(len(alphabets)):
        if appearances[i] > 0:
            result.append((alphabets[i], appearances[i]))

    # Return result
    return result

print(countAllLetters(line))