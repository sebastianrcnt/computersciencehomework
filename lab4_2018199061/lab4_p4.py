i = 1
while i <= 100:
    digit1 = i % 10
    digit2 = (i//10) % 10
    digit3 = (i//100) % 10
    # print(digit3, digit2, digit1)
    if i < 10:
        print(f'  {digit1}', end = '')
    if 10 <= i < 100:
        print(f' {digit2}{digit1}', end = '')
    if i == 100:
        print('100', end = '')
        break
    if i % 10 == 0:
       print('\n')
    i = i + 1