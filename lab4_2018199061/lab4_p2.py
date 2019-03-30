num = 1
sum = 0
while num != 0:
    num = int(input('Your number: '))
    if num <= 100:
        sum += num
    print(sum)

print(f'Sum: {sum}')