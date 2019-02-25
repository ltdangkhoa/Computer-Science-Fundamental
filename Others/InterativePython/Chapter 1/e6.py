"""
In the definition of fractions we assumed that negative fractions
have a negative numerator and a positive denominator.
Using a negative denominator would cause some of the relational
operators to give incorrect results. In general, this is an unnecessary constraint.
Modify the constructor to allow the user to pass a negative
denominator so that all of the operators continue to work properly.
"""


class Fraction:
    """
    Usage: f = Fraction(1, 2)
    """

    def __init__(self, _fa, _fb, test=False):
        del test  # Unused variable test

        if _fa % 1 != 0 or _fb % 1 != 0:
            raise ValueError("Must be integer")
        else:
            self.num = _fa
            self.den = _fb
            if (self.den < 0 < self.num) or (self.den < 0 and self.num < 0):
                self.den = self.den * -1
                self.num = self.num * -1
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

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

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

    def __gt__(self, x):
        """Overide default greater than (>) operators"""
        return self.num * x.den > x.num * self.den

    def __ge__(self, x):
        """Overide default greater than or equal (>=) operators"""
        return self.num * x.den >= x.num * self.den

    def __lt__(self, x):
        """Overide default less than (<) operators"""
        return self.num * x.den < x.num * self.den

    def __le__(self, x):
        """Overide default less than or equal (<=) operators"""
        return self.num * x.den <= x.num * self.den

    def __ne__(self, x):
        """Overide default not equal (!=) operators"""
        return self.num * x.den != x.num * self.den

    def __eq__(self, x):
        """Overide default equal (==) operators"""
        return self.num * x.den == x.num * self.den


def demo():
    """Run this implementation"""
    f_1 = Fraction(1, -4)
    f_2 = Fraction(1, 2)
    print(f_1)
    f_3 = f_1 / f_2
    print(f_3)


demo()
