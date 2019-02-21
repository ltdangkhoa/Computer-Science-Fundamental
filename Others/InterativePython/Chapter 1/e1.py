"""
Implement the simple methods getNum and getDen
that will return the numerator and denominator of a fraction
"""


class Fraction:
    """Define fraction numerator and fraction denominator"""

    def __init__(self, _fa, _fb):
        self.num = _fa
        self.den = _fb

    def getNum(self):
        """Return the numerator of fraction"""
        return self.num

    def getDen(self):
        """Return the denominator of fraction"""
        return self.den


def demo():
    """Run this implementation"""
    my_fraction = Fraction(3, 4)
    print(my_fraction.getNum())
    print(my_fraction.getDen())


demo()
