class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator


    def show(self):
        print(f'{self.numerator} / {self.denumerator}')

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denumerator)

    def __add__(self, other):
        # print(other)
        newnumerator = self.numerator * other.denumerator + self.denumerator * other.numerator
        newdenumerator = self.denumerator * other.denumerator
        return Fraction(newnumerator, newdenumerator)

    def __sub__(self, other):
        newnumerator = self.numerator * other.denumerator - self.denumerator * other.numerator
        newdenumerator = self.denumerator * other.denumerator
        return Fraction(newnumerator, newdenumerator)

    def __mul__(self, other):
        newnumerator = self.numerator * other.numerator

        newdenumerator = other.denumerator * self.denumerator

        return Fraction(newnumerator, newdenumerator)

    def __floordiv__(self, other):
        newnumerator = self.numerator // other.numerator
        # print(newnumerator)
        newdenumerator = other.denumerator // self.denumerator
        # print(newdenumerator)
        return Fraction(newnumerator, newdenumerator)

# num_fraction = Fraction(3,5)
# num_fraction.show()

# print(num_fraction)
addf1 = Fraction(1,4)
addf2 = Fraction(1,2)
addf3 = addf1 + addf2
print(addf3)

subf1 = Fraction(1,2)
subf2 = Fraction(1,3)
subf3 = subf1 - subf2
print(subf3)

mulf1 = Fraction(2,3)
mulf2 = Fraction(3,2)
mulf3 = mulf1 * mulf2
print(mulf3)

floordivf1 = Fraction(3,4)
floordivf2 = Fraction(4,5)
floordivf3 = floordivf1 // floordivf2
print(floordivf3)