ans = int(input('Enter an integer: '))
for i in range(1,ans+1):
    n = ans + 1 - i
    print(' '*(i-1)+'*'*(2*n-1))