"""
In many ways it would be better if all fractions were
maintained in lowest terms right from the start.
Modify the constructor for the Fraction class
so that GCD is used to reduce fractions immediately.
Notice that this means the __add__ function
no longer needs to reduce. Make the necessary modifications
"""


def gcd(_a, _b):
    """
    GCD function out of the class, can be improved with class inner auto_gcd()
    """
    while _a % _b != 0:
        last_a = _a
        last_b = _b
        _a = last_b
        _b = last_a % last_b
    return _b


class Fraction:
    """
    Define fraction numerator and fraction denominator.
    The constructor will calculate the GCD (Greatest Common Divisor)
    of fraction and return reduced fraction
    """

    def __init__(self, _fa, _fb):
        self.num = _fa
        self.den = _fb
        self.auto_gcd()

    def auto_gcd(self):
        """Improve the implement of GCD"""
        _a = self.num
        _b = self.den
        while _a % _b != 0:
            last_a = _a
            last_b = _b
            _a = last_b
            _b = last_a % last_b

        self.num = int(self.num / _b)
        self.den = int(self.den / _b)

    def getNum(self):
        """Return the numerator of fraction"""
        return self.num

    def getDen(self):
        """Return the denominator of fraction"""
        return self.den

    def __add__(self, _x):
        """Overide default add (+) function"""
        nfa = self.num * _x.den + _x.num * self.den
        nfb = self.den * _x.den
        return Fraction(nfa, nfb)


def demo():
    """Run this implementation"""
    f_1 = Fraction(2, 4)
    f_2 = Fraction(60, 90)
    f_3 = f_1 + f_2
    print(f_3.num)
    print(f_3.den)


demo()
