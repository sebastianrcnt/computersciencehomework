# Init
# Open File and split each line into list
datafile = open('data.txt', 'r')
data = datafile.read()
datalist = data.split('\n')

# Convert every item into integer
for i in range(len(datalist)):
    datalist[i] = int(datalist[i])

# Add substituted values to datalist
datalist = [datalist[0]] + datalist + [datalist[-1]]

# avlist to contain averaged result
avlist = []

# add average to avlist
for i in range(1, len(datalist)-1):
    avlist.append((datalist[i-1]+datalist[i]+datalist[i+1])/3)

# print result
print(avlist)