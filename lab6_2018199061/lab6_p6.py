# Get User Input
ans = int(input('Enter the limit L: '))

# Loop until user input is 0
while ans != 0:
    SUM = 0.0
    for i in range(1, ans+1):  # add up all the numbers under ans and ans
        SUM = SUM + 1/i

    # print result
    print('Sum of the initial {} term(s): {:.6f}'.format(ans, sum))
    ans = int(input('Enter the limit L: '))
