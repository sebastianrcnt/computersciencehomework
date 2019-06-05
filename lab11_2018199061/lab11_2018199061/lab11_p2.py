import time
import copy

size = 20  # size of the 2D cellular automaton
work = []


# Functions
def printSep():
    '''Print a separator'''
    for ctr in range(0, size + 2):
        print('-', end='')
    print('')


def printWorld(world):
    '''Print one generation.
       Must use printSep() above to print the separators.
    '''
    printSep()  # upper separator
    for i in range(len(world)):
        print('|', end='')  # left bar
        # print row
        for item in world[i]:
            if item == 0:
                print(' ', end='')
            elif item == 1:
                print('x', end='')
        print('|', end='')  # right bar
        print(' row ', i, sep='', end='\n')  # row indicator
    printSep()  # lower separator


#
# Main program
#

# Get user input for grid sidelength
ans = input('Grid sidelength (default 20): ')


try:
    # make sure that size is equal to or bigger than 20
    ans = int(ans)
    if ans >= 20:
        size = ans
    else:
        size = 20
except:  # if input invalid, size = 20(default)
    size = 20

# Get Max generations
# Ask until valid maxgen input
maxgen = 0
while maxgen <= 0:
    try:
        maxgen = int(input('Max generation: '))
    except:
        pass


# Initialize work
default_row = [0]*size  # make a empty row with a length of size ([0,0,...,0,])
for i in range(size):
    work.append(copy.deepcopy(default_row))  # append its copy to work

# Set initial conditions
initialCoords = [(0, 1), (1, 1), (2, 1), (10, 10), (10, 11), (10, 12), (11, 10), (12, 10), (12, 11), (12, 12)]
for coord in initialCoords:
    work[coord[0]][coord[1]] = 1


# Compute:
gen = 0
while gen <= maxgen:  # Keep until the max generation
    printWorld(work)
    tmp = copy.deepcopy(work)  # Deepcopy work
    for i in range(len(tmp)):  # Iterating row
        for j in range(len(tmp[i])):  # Iterating Items
            # print('-'*20)
            # print(f'evaluating {i}, {j}')
            surroundingTotal = 0
            surroundingCoords = \
                [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), \
                 (i, j - 1), (i, j + 1), \
                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

            # Check every surrounding cell if it is alive, dead or doesn't exsist
            for coord in surroundingCoords:
                # Catch IndexErrors(overflow)
                try:
                    # coordinates with negative indexes will be ignored
                    if (coord[0] < 0) or (coord[1] < 0):
                        # print(f'coord {coord} doesn\'t exist!')
                        pass
                    else:
                        if tmp[coord[0]][coord[1]] == 1:
                            # print(f'coord {coord} is alive!')
                            surroundingTotal = surroundingTotal + 1
                        elif tmp[coord[0]][coord[1]] == 0:
                            # print(f'coord {coord} is dead!')
                            pass
                except IndexError:
                    # print(f'overflow: coord {coord} doesn't exsist!')
                    pass

            # Determine whether cell is alive/dead at the next generation
            # Catch IndexErrors(overflow)
            try:
                # Alive Cells
                if tmp[i][j] == 1:
                    if not (2 <= surroundingTotal <= 3):
                        # print(f'alive cell ({i}, {j}) with {surroundingTotal} neighbors dead!')
                        work[i][j] = 0
                    else:
                        # print(f'alive cell ({i}, {j}) with {surroundingTotal} neighbors is alive!')
                        pass
                # Dead Cells
                elif tmp[i][j] == 0:
                    if surroundingTotal == 3:
                        # print(f'dead cell ({i}, {j}) with {surroundingTotal} neighbors is alive!')
                        work[i][j] = 1
                else:
                        # print(f'dead cell ({i}, {j}) with {surroundingTotal} neighbors is dead!')
                        pass
            except IndexError:
                # Index out of range
                pass
    # Increment generation
    gen = gen + 1

    # Sleep
    time.sleep(1)