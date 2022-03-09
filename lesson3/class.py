class Dino:

    def __init__(self, dino_name, legkie, brine):

        self.dino_name = dino_name
        self.legkie = legkie
        self.brine = brine

    def __str__(self):
        return f"{self.dino_name} {self.legkie} {self.brine}

    def get_name(self):
        print("i am smart!")
class Shark:
    def __init__(self, shark_name, jabri, sila):
        self.shark_name = shark_name
        self.jabri = jabri
        self.sila = sila

    def get_dino_name(self):
        print("i am speed!")

class Dinoshark(Dino, Shark):
    pass
class Human(Dinoshark):
    def __init__(self, dino_name, legkie, brine):
        super().__init__(dino_name, legkie, brine)
        self.__mro__ = None

    pass

human = Human("dinaobek", "normaln", 'false')
print(human.sila)
print(human.__mro__)