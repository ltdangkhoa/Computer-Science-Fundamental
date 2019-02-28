"""
Modify the constructor for the fraction class so that
it checks to make sure that the numerator and denominator
are both integers.
If either is not an integer the constructor should raise an exception
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
    f_1 = Fraction(1.0, 4.3)
    print(f_1.num)
    print(f_1.den)


demo()
