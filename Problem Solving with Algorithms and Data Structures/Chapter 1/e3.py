"""
Implement the remaining simple arithmetic operators
(```__sub__```, ```__mul__```, and ```__truediv__```)
"""


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

    def __sub__(self, _x):
        """Overide default sub (-) function"""
        nfa = self.num * _x.den - _x.num * self.den
        nfb = self.den * _x.den
        return Fraction(nfa, nfb)

    def __mul__(self, _x):
        """Overide default multiply (*) function"""
        nf_num = self.num * _x.num
        nf_den = self.den * _x.den
        return Fraction(nf_num, nf_den)

    def __truediv__(self, _x):
        """Overide default truediv (/) function"""
        return self.__mul__(Fraction(_x.den, _x.num))


def demo():
    """Run this implementation"""
    f_1 = Fraction(1, 4)
    f_2 = Fraction(2, 4)
    f_3 = f_1 - f_2
    print(f_3.num)
    print(f_3.den)
    f_3 = f_1 * f_2
    print(f_3.num)
    print(f_3.den)
    f_3 = f_1 / f_2
    print(f_3.num)
    print(f_3.den)


demo()
