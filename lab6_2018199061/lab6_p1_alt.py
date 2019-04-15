ans = input('Enter a first name and last name: ')
anssplit = ans.split()
firstName = anssplit[0]
lastName = anssplit[1]
print(firstName, lastName)

firstNameStartIndex = 0
lastNameStartIndex = 0

for i in range(len(ans)):
    if ans[i] != ' ':
        firstNameStartIndex = i

for i in range(firstNameStartIndex+len(firstName),len(ans)):
    if ans[i] != ' ':
        lastNameStartIndex = firstNameStartIndex + len(firstName) + i

print(firstNameStartIndex, lastNameStartIndex)