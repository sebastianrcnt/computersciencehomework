# init
ans = ''
res = []

# get user input until user inputs 'q'
while ans != 'q':
    ans = input('Enter a word (q to quit): ')
    # check whether the first character(ans[0]) is repeated in the rest of the answer
    if ans[0] in ans[1:]:
        res.append(ans)

# Sort Result
res.sort()

# Print Result
print(res)
