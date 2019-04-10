product = 1
num = int(input('Enter first number: '))
product = product * num
while num != 0:
    num = int(input('Enter next number: '))
    if num == 0:
        break
    product = product * num
print('product = ', product) 