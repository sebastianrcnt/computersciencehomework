# Get ISBN
isbn = input('Enter an ISBN: ')

# Split ISBN
isbnSplit = isbn.split('-')

# Print Result
print(format(isbnSplit[0], '.<20')+'GS1 prefix')
print(format(isbnSplit[1], '.<20')+'Group identifier')
print(format(isbnSplit[2], '.<20')+'Publisher code')
print(format(isbnSplit[3], '.<20')+'Item number')
print(format(isbnSplit[4], '.<20')+'Check digit')
