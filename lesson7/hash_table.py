# type = input("Введите марку: ")

class Car:

    def __init__(self, model, title):
        self.model = model
        self.title = title


class Bmw(Car):

    def __init__(self, model, title):
        super().__init__(model, title)


class Mercedes(Car):

    def __init__(self, model, title):
        super().__init__(model, title)


class Audi(Car):

    def __init__(self, model, title):
        super().__init__(model, title)

class Bentley(Car):

    def __init__(self, model, title):
        super().__init__(model, title)





bmw = [
    Bmw('e34', 'bmw'),
    Bmw('e34', 'bmw'),
    Bmw('e34', 'bmw')
]
mercedes = [
    Mercedes('e55', 'mers'),
    Mercedes('e55', 'mers'),
    Mercedes('e55', 'mers')
]
audi = [
    Audi('rs6', 'audi'),
    Audi('rs6', 'audi')
]

bentley = [
    Bentley('phantom', 'bentley'),
]

mark = input("Введите марку: ")

hash_table = {
    "mercedes": mercedes,
    "bmw": bmw,
    "audi": audi,
    "bentley": bentley
}
print(hash_table[mark])

