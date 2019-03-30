# Take user input
ans = int(input('Enter a number: '))

digit = 1 # counter
ansCopy = ans # make a copy of ans

# determine how many digit(s) that ans contain(s)
while ansCopy >= 10: 
    ansCopy = ansCopy // 10
    digit = digit + 1

# print the result
if digit == 1:
    print(f'The number {ans} contains 1 digit')
else:
    print(f'The number {ans} contains {digit} digits')