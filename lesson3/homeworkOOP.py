class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator


    def __add__(self, other):
        last_num = self.numerator
        last1_num = self.denumerator
        self.numerator += other
        self.denumerator += other
        return f'{last_num} + {other} = {self.numerator}, \n{last1_num} + {other} = {self.denumerator}'


    def __sub__(self, other):
        last_num = self.numerator
        last1_num = self.denumerator
        self.numerator -= other
        self.denumerator -= other
        return f'{last_num} - {other} = {self.numerator}, \n{last1_num} - {other} = {self.denumerator}'


    def __mul__(self, other):
        last_num = self.numerator
        last1_num = self.denumerator
        self.numerator *= other
        self.denumerator *= other
        return f'{last_num} * {other} = {self.numerator}, \n{last1_num} * {other} = {self.denumerator}'


    def __floordiv__(self, other):
        last_num = self.numerator
        last1_num = self.denumerator
        self.numerator //= other
        self.denumerator //= other
        return f'{last_num} * {other} = {self.numerator}, \n{last1_num} * {other} = {self.denumerator}'

num_fraction = Fraction(10, 20)


print(num_fraction + 2)
print(num_fraction - 2)
print(num_fraction * 2)
print(num_fraction // 2)
