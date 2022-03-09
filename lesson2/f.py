class Person:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance
e = Jack('s', 'b','123456',99)

class Vito(Jack):
    num = 70
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def cat(self):
        r = e.balance - self.num
        t = self.balance + r
        print(f"'cat', {t}")

brad = Vito('w', 'r', '789', 55)
Vito.cat()

