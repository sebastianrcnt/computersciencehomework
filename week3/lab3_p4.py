import random
numbers = []
for i in range(6):
	numbers.append(random.randint(1,45))
print(f'Lotto numbers of the week: {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]} {numbers[5]}')