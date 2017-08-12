class Rational:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __add__(self, other):
        return Rational((self.numerator * other.denominator + self.denominator * other.numerator),
                        (self.denominator * other.numerator))

    def __mul__(self, other):
        return Rational((self.numerator * other.numerator), (self.denominator * other.denominator))

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


r1 = Rational(1, 2)
r2 = Rational(3, 4)

print(r1)
print(r1 + r2)
print(r1 * r2)
