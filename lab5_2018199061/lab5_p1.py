ans = float(input("Enter a number: "))  # get first input
if ans <= 0: # if first input not positive number
    print('No positive number was entered')
else: # if first input is positive number
    while True: # infinite loop.
        ans2 = float(input("Enter a number: ")) 
        ans = max(ans, ans2) # ans will store the maximum number among the numbers that user typed in
        if ans2 <= 0: # break if input is not positive number
            break
    print('The largest number entered was {0:.2f}'.format(ans)) # format and print 'ans'