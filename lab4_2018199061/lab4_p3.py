ans = int(input('Enter a number: '))

digit = 1
ansCopy = ans

while True:
    if ansCopy < 10:
        break
    ansCopy = ansCopy // 10
    digit = digit + 1

if digit == 1:
    print(f'The number {ans} contains 1 digit')
else:
    print(f'The number {ans} contains {digit} digits')