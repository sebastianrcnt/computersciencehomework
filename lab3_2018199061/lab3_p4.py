# import modules
import random

# make a list to store the generated integers
numbers = []

# add integers to numbers
for i in range(6):
	numbers.append(random.randint(1,45))

# print numbers
print(f'Lotto numbers of the week: {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]} {numbers[5]}')