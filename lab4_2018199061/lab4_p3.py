# Take user input
ans = int(input('Enter a number: '))

digit = 1 # counter variable. starts with 1
ansCopy = ans # make a copy of ans. the user input 'ans' will be used to print the input number to screen, and ansCopy will be used to evaluate how many digits is ans.

# the while loop below determines how many digit(s) is ansCopy.
while ansCopy >= 10: 
    ansCopy = ansCopy // 10 # ansCopy is divided by 10 without remainders (ex) 532 // 10 => 53
    digit = digit + 1
    # every time this loop is executed, digit increases by 1.

# print the result
if digit == 1: # if ans is one-digit number
    print(f'The number {ans} contains 1 digit')
else: # if ans is two or more digit number
    print(f'The number {ans} contains {digit} digits')