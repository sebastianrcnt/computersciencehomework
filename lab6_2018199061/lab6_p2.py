# Init
slashIndex = 0

# Get user input
ans = input('Enter a fraction: ')
step = 0

# Remove all space in ans
ansWithoutSpace = ''
for ch in ans:
    # when ch is a non-space character, ch is added to ansWithoutSpace
    if ch != ' ':
        ansWithoutSpace = ansWithoutSpace + ch

# Find where the slash is located in ansWithoutSpace
for i in range(len(ansWithoutSpace)):
    if ansWithoutSpace[i] == '/':
        slashIndex = i

numerator = int(ansWithoutSpace[0:slashIndex])  # the string before /
denominator = int(ansWithoutSpace[slashIndex+1:])  # the string after /

if numerator % denominator == 0:
    # if numerator is a multiple of the denominator, print the value
    print('In lowest terms: ' + str(int(numerator/denominator)))
else:
    # Find the GCD and change into the lowest terms
    m = numerator
    n = denominator
    r = m % n
    while r != 0:
        r = m % n
        m = n
        n = r
    gcd = m

    # print the result
    print('In lowest terms: '+str(int(numerator/gcd))+'/'+str(int(denominator/gcd)))
