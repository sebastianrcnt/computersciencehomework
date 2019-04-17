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
    # find the position where a non-space character appears, which is the starting index of the first name
    if ans[i] != ' ':
        firstNameStartIndex = i
        break

# Count the start and end of First name.
for i in range(firstNameStartIndex, len(ans)): # i starts from the starting index of the first name which is obtained above.
    # find the position where a space character appears, which is the index of the end of the first name - 1
    if ans[i] == ' ':
        firstNameEndIndex = i - 1
        break

# Count spaces from the end of first name until the start of Last name
for i in range(firstNameEndIndex + 1, len(ans)):
    if ans[i] != ' ':
        lastNameStartIndex = i
        break

# Count the start and end of Last name.
for i in range(lastNameStartIndex, len(ans)):
    if ans[i] == ' ':  # if there is space after the last name
        lastNameEndIndex = i - 1
        break
    elif i == len(ans):  # if there is no space after the last name(=if i reaches len(ans) so that this loop ends without meeting a space)
        lastNameEndIndex = len(ans)

# Print the result in the given format
print(firstName + ', ' + lastName[0] + '.')
