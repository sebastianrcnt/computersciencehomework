from lab12_p4 import Fraction

f1 = Fraction(2,12)
f2 = Fraction(1,6)
f2.num = 2

print('f1:', f1)
print('f2:', f2)

f2.reduce()
print('f2:', f2)

f2.adjust(3)
print('f2:', f2)

f3 = Fraction(148,-924)
print('f3:', f3)