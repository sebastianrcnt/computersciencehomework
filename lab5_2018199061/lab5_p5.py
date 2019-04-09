# P4. Write a Python program that prompts the user to enter a list of first names and stores them in a list. The program should display how many times the letter 'a' appears within the list.
li = []
while True:
    ans = input('Enter a name (q to quit): ')
    if ans == 'q':
        break
    li.append(ans)

sol = 0
for i in li:
    sol = sol + i.count('a') + i.count('A')

print(f"Apperance of letter 'a': {sol}")