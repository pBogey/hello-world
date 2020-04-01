"""
New Data Type - Fraction
Bogdan Prădatu - from how to think like a computer scientist
11.07.2019
"""

def gcd(m,n):
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)

class Fraction:
    def __init__(self, numerator, denominator=1):
        g = gcd(numerator,denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __str__(self):
        return f"{self.numerator:d}/{self.denominator:d}"
        #return ("%d/%d" %(self.numerator, self.denominator))

    def __add__(self,other):
        if type(other) == int:
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    __radd__ = __add__

    def __mul__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return Fraction(self.numerator*other.numerator,
                        self.denominator*other.denominator)

    __rmul__ = __mul__

    def __cmp__(self,other):
        diff = (self.numerator * other.denominator -
                other.numerator * self.denominator)
        return diff

spam = Fraction(5,6)
print("The fraction is", spam)
print(Fraction(5,6)*Fraction(3,4))
print(3*Fraction(2))
print(Fraction(5,6)+Fraction(5,6))
