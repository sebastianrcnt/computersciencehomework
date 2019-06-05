def getFile():
    '''
        Returns the file name and associated file object for reading the
        file  as tuple of the form (file_name, input_file).
    '''
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print ('Unable to open input file, please reenter')
    return (file_name, input_file)

def countWords(input_file):
    '''
    Counts all appearances of every appeared word and return it as a dictionary

    Parameters:
        input_file: input file
    Return:
        occurrenceDict: dictionary(value(int),key(string))
    '''
    word_delimiters = (' ', ',', ';', ':', '.', '\n',
                       '"', "'", '(', ')')
    words = []

    for line in input_file:
        # Read line and replace all delimiters to ' '(blank character)
        for delimiter in word_delimiters:
            line = line.replace(delimiter, ' ')

        # Lower and Split line and add its items into words
        words = words + line.lower().split()

    occurrenceDict = {}

    # Find number of occurrences of each word in word and add it to occurrenceDict
    for word in words:
        # Already existing words will be overwritten, but it will not change the result.
        occurrenceDict[word] = words.count(word)

    # Return the dictionary
    return occurrenceDict

# Get File
file_name, input_file = getFile()

# Write new file
new_file_name = file_name[:-3] + 'wc'
out = open(new_file_name, 'w')

# Get Occurrence Dictionary
occurrenceDict = countWords(input_file)
keylist = list(occurrenceDict.keys())

# Sort keylist to write line in alphabetic order
keylist.sort()

# Write Each Line
for i in range(len(keylist)):
    word = keylist[i]
    out.write(f'{word}: {occurrenceDict[word]}')
    # Seperate each line with newline character
    # No newline at the end of the file
    if i != len(occurrenceDict.keys()) - 1:
        out.write('\n')

# Close and Save the file
out.close()