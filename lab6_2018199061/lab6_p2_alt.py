ans = input('fraction:')
ans = [x for x in ans if x !=' ']

slash = ans.index('/')
numeratorList = ans[:slash]
denominatorList = ans[slash+1:]

numeratorStr = ''
for i in numeratorList:
    numeratorStr = numeratorStr + i

denominatorStr = ''
for i in denominatorList:
    denominatorStr = denominatorStr + i

numerator = int(numeratorStr)
denominator = int(denominatorStr)

if numerator % denominator == 0:
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

    print(f'In lowest terms: {int(numerator/gcd)}/{int(denominator/gcd)}') # int 반드시 쓸것!