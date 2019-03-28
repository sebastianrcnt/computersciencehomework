num1 = int(input('Your number: '))
num2 = int(input('Your number: '))
num3 = int(input('Your number: '))
num4 = int(input('Your number: '))

sum = 0

if num1 < 100:
    sum += num1
if num2 < 100:
    sum += num2
if num3 < 100:
    sum += num3
if num4 < 100:
    sum += num4

print('Sum: %d' % sum)
