Q1 :
(a) True
(b) True
(c) False
(d) False

Q2 :
(a) False
(b) True
(c) True
(d) False
(e) True

Q3 :
(a) : (0 <= num) and (num < 100)
(b) : (num < 100) and (num >= 0) or (num == 200)
(c) : ('Thompson' in last_names) or ('Wu' in last_names)
(d) : ('Thompson' not in last_names) and ('Wu' not in last_names)

Q4 : the given code has the following errors.
1. Type conversion is missing. line 2 and 5 should be changed to:
num = int(input('Enter first number: '))
2. Input message is wrong. line 5 should be changed to:
num = int(input('Enter next number: '))
3. Sentinel value 0 is unintentionally multiplied at the last loop of the program. Therefore we should add an if statement with break command between line 5 and 6 to escape the while loop right before the sentinel value is multiplied to 'product'.
4. The first user input is not multiplied to 'product'. product = product * num should be added between line 2 and 3.

Considering 1 ~ 4, the code will look like this:

product = 1
num = int(input('Enter first number: '))
product = product * num
while num != 0:
    num = int(input('Enter next number: '))
    if num == 0:
        break
    product = product * num
print('product = ', product) 
