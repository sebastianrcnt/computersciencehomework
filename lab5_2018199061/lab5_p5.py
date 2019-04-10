li = []

# User input
while True:
    ans = input('Enter a name (q to quit): ')
    if ans == 'q':
        break
    li.append(ans)

# Count 'a' 'A'
sol = 0
for i in li: # for every item in 'li'
    sol = sol + i.count('a') + i.count('A') # add number of apperances of 'a' or 'A' in sol

# Print
print(f"Apperance of letter 'a': {sol}")