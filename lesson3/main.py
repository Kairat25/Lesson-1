class Balance:

    def __init__(self, num, username):
        self.num = num
        self.username = username
        print(num, username)

    def __str__(self):
        return f"{self.username} balance = {self.num}"



    def __add__(self, other):
        print("magic metod __add__")
        self.num += other
        return self.num


    def __sub__(self, other):
        print("magic metod __sub__")
        self.num -= other
        return self.num

    def __mul__(self, other):
        print("magic metod __mul__")
        self.num *= other
        return self.num
    def __floordiv__(self, other):
        previos_num = self.num
        self.num //= other
        return f"{previos_num} // {other} = {self.num}"

jack_balance = Balance(5000, 'Vito')
vito_balance = Balance(1000, 'Bred')


print(jack_balance + 40)
print(jack_balance // 2)

