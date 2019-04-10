res = [] # variable to store integers
while True:
    ans = int(input('Enter an integer: '))
    if ans == 0:
        break # escape loop when ans is 0
    if ans <= 100: # under 100 append
        res.append(ans)
    else: # over 100 append 'over'
        res.append('over')
print(res) # print list