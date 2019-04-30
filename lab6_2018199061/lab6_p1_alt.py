ans = input('enter first name and last name :')
splittedAns = ans.split(' ')
splittedAns = [item for item in splittedAns if item != '']
print(splittedAns)
firstName = splittedAns[0]; print(firstName)
lastName = splittedAns[1]; print(lastName)
print(lastName,', ',firstName[0],'.',sep='')