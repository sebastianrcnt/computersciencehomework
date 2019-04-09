# initialize variables
num = 1 # variable 'num' to store integer from the user input
sum = 0 # variable 'sum' to store the sum of numbers

while num != 0: # keep asking for numbers until user inputs 0
    num = int(input('Your number: '))
    if num <= 100: # if number is equal or smaller than 100,
        sum += num # add user input to 'sum'

print(f'Sum: {sum}') # print the result