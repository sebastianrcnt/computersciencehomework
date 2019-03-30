i = 1 # counter i
while i <= 100:
    digit1 = i % 10  # the first digit of the number
    digit2 = (i//10) % 10 # the second digit of the number
    digit3 = (i//100) % 10 # the third digit of the number

    if i < 10: # if i is an one-digit number
        print(f'  {digit1}', end = '') # 2 spaces and first digit
    if 10 <= i < 100: # if i is a two-digit number
        print(f' {digit2}{digit1}', end = '') # 1 space and second and first digit
    if i == 100: # if i is 100 
        print('100', end = '')  # 1 space and second and first digit
        break # end while loop when i reaches 100
    
    if i % 10 == 0: # add a new line after 10, 20, ... , 90. a new line is not added after 100 because 'break' at line 13 ends this loop
       print('\n')
    i = i + 1 # counter increases by 1