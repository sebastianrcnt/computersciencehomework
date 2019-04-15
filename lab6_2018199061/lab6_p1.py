# Get user input for Name
ans = input('Enter a first and last name: ')

# Initialize variables to store the start and end indexes of first and last name
firstNameStartIndex = 0
lastNameStartIndex = 0
firstNameEndIndex = 0
lastNameEndIndex = 0

# Split variables to get the first and second word in ans, which is individually first name and last name.
anssplit = ans.split()
firstName = anssplit[0]
lastName = anssplit[1]

# Count spaces until the start of First name
for i in range(len(ans)):
    print(f'part1 i : {i}, ans[i]: {ans[i]}')
    if ans[i] != ' ':
        firstNameStartIndex = i
        break

# Count spaces from First name to the end of First name.
for i in range(firstNameStartIndex, len(ans)):
    print(f'part2 i : {i}, ans[i]: {ans[i]}')
    if ans[i] == ' ':
        firstNameEndIndex = i - 1
        break

# Count spaces from the end of first name until the start of Last name
for i in range(firstNameEndIndex + 1, len(ans)):
    print(f'part3 i : {i}, ans[i]: {ans[i]}')
    if ans[i] != ' ':
        lastNameStartIndex = i
        break

for i in range(lastNameStartIndex, len(ans)):
    print(f'part4 i : {i}, ans[i]: {ans[i]}')
    if ans[i] == ' ':
        lastNameEndIndex = i - 1
        break
    elif i == len(ans):
        lastNameEndIndex = len(ans)

print(f'First Name index: {firstNameStartIndex}~{firstNameEndIndex}')
print(f'First Name index: {lastNameStartIndex}~{lastNameEndIndex}')
print(f'First Name : {firstName}, Last Name : {lastName}')
print(f'{firstName}, {lastName[0]}.')