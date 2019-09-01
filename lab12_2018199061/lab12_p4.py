#
# Fraction class:
#

class Fraction(object):
    """
    Class to represent a number as a fraction
    
    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """ Method to construct a Fraction object """
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
           raise ValueError('requires type int')
        # Check that denominator is non-zero:
        if d == 0:
           raise ZeroDivisionError('requires non-zero denominator')
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d
        self.reduce()


    def __str__(self):
        """ Returns a string representation of the fraction object (self) """
        return str(self.num) + '/' + str(self.denom)


    def __mul__(self, other):
         """ Returns new Fraction representing self * other """
         new_num = self.num * other.num
         new_denom = self.denom * other.denom
         return Fraction(new_num, new_denom)


    def __add__(self, other):
         """ Returns new Fraction representing self + other """
         new_num = self.num * other.denom + other.num * self.denom
         new_denom = self.denom * other.denom
         return Fraction(new_num, new_denom)


    def __float__(self):
         """ Returns a float-value of the Fraction object"""
         return self.num / self.denom # result of / is of type float

    def reduce(self):
        """Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD). Also removes the signs if both numerator and denominator are negative. Whole numbers (1, 2, ...) are represented as
        1/1, 2/1, 3/1, ...
        """
        # assign absolute value of numerator and denominator to a new variable
        abs_num = abs(self.num)
        abs_denom = abs(self.denom)

        # get a gcd
        GCD = 1
        i = 1
        while i <= min(abs_num, abs_denom):
            if (abs_num % i == 0) and (abs_denom % i == 0):
                GCD = i
            i = i + 1
        if self.num < 0 and self.denom < 0:
            self.num = abs_num // GCD
            self.denom = abs_denom // GCD
        else:
            self.num = self.num // GCD
            self.denom = self.denom // GCD

    def adjust(self, factor):
        """Multiplies numerator and denominator by factor."""
        self.num = self.num * factor
        self.denom = self.denom * factor