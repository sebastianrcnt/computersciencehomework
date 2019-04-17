# Import Modules
from operator import itemgetter

# Init
fruitList = []

# Get first input and terminate if 'q' is inputted.
ans = input('Enter a fruit type (q to quit): ')
if ans == 'q':
    print('No data received, exiting.')
else:
    # keep asking until user inputs 'q'
    while ans != 'q':
        weight = int(input('Enter the weight in kg: '))
        # make list fruitNames, whose items are the names of fruitList
        fruitNames = []
        for item in fruitList:
            fruitNames.append(item[0])

        # check whether the answer is in fruitNames
        if ans in fruitNames:
            for i in range(len(fruitList)):
                if ans == fruitList[i][0]:
                    fruitList[i][1] = fruitList[i][1] + weight
                    # add the weight on the weight of the corresponding fruit item sublist([fruit name, fruit weight])
        else:
            fruitList.append([ans, weight])  # add a new type of fruit and its weight

        # ask for fruit type
        ans = input('Enter a fruit type (q to quit): ')
        # this is located at the end of the while loop since the program should proceed without asking weight.
    
    # Sort the list and Print
    fruitList.sort(key=itemgetter(0))
    for item in fruitList:
        print(item[0]+', '+str(item[1])+'kg.')
