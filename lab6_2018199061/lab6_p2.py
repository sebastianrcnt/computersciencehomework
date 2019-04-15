
ans = input('Enter a fraction: ')
step = 0

# delete all spaces in ans
while ' ' in ans: # loop until ans has no space
    for i in range(len(ans)): # removes the first space
        if ans[i] == ' ':
            ans = ans[:i] + ans[i+1:] # when it meets space, it removes the space by slicing and merging 
            break # escapes the for loop

# print the answer
print(ans)