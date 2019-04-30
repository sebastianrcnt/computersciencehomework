Q1:
(a) is not valid since there is no third parameter provided.
(b) is valid since it produces no errors, but the result will not be the average of n1, n2, n3, n4 and n5
(c) is valid
(d) is valid, but the returned value will not be assigned to a variable. it will only be printed on the console.
(e) is valid, but just calling a function like this will not be assigned or printed in the console.

Q2:
(a) is proper, and result will be 10
(b) is not proper since n1 is not integer value.
(c) is proper, and result will be 10
(d) is proper, and result will be 10
(e) is improper because when i call gcd like 'gcd(c,b)' while c=30, b=20, the first argument n1(in here, c) should be less than n2(in here, b).

Q3:
l1 = [1,2]
l2 = [0,5]
l3 = ['foo']
l1.append(l3)
# l1 = [1,2,['foo']]

l2[0] = l3
# l2 = [['foo'], 5]

print(id(l2[0]) == id(l1[2]))
# True
