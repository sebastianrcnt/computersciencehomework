ans = int(input('Enter an integer: ')) # get input
for i in range(1,ans+1): # when i starts from 1 and increases by 1 until ans (1 2 .. ans-1 ans)
    # n : number of '*' in each row (=ans+1-i)
    # i-1 : number of ' ' in each row
    n = ans + 1 - i
    print(' '*(i-1)+'*'*(2*n-1))