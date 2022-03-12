class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator


    def show(self):
        print(f'{self.numerator} / {self.denumerator}')

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denumerator)

    # def __init__(self, numerator, denumerator):
    #     self.numerator = numerator
    #     self.denumerator = denumerator

    #
    # def __add__(self, other):
    #     last_num = self.numerator
    #     last1_num = self.denumerator
    #     self.numerator += other
    #     self.denumerator += other
    #     return f'{last_num} + {other} = {self.numerator}, \n{last1_num} + {other} = {self.denumerator}'
    #
    #
    # def __sub__(self, other):
    #     last_num = self.numerator
    #     last1_num = self.denumerator
    #     self.numerator -= other
    #     self.denumerator -= other
    #     return f'{last_num} - {other} = {self.numerator}, \n{last1_num} - {other} = {self.denumerator}'
    #
    #
    # def __mul__(self, other):
    #     last_num = self.numerator
    #     last1_num = self.denumerator
    #     self.numerator *= other
    #     self.denumerator *= other
    #     return f'{last_num} * {other} = {self.numerator}, \n{last1_num} * {other} = {self.denumerator}'
    #
    #
    # def __floordiv__(self, other):
    #     last_num = self.numerator
    #     last1_num = self.denumerator
    #     self.numerator //= other
    #     self.denumerator //= other
    #     return f'{last_num} * {other} = {self.numerator}, \n{last1_num} * {other} = {self.denumerator}'

    def __add__(self, other):
        # print(other)
        a = f'{self.numerator} / {self.denumerator} + {other.numerator} / {other.denumerator}'
        newnumerator = self.numerator * other.denumerator + self.denumerator * other.numerator
        newdenumerator = self.denumerator * other.denumerator
        return f'{a} = {newnumerator}/{newdenumerator}'


num_fraction = Fraction(10, 20)


addf1 = Fraction(1,4)
addf2 = Fraction(1,2)
addf3 = addf1 + addf2
print(addf3)


# print(num_fraction - 2)
# print(num_fraction * 2)
# print(num_fraction // 2)
