class Steklo:

    def __init__(self, strength , morf, color, form):
        self.strength = strength
        self.morf = morf
        self.color = color
        self.form =form

    def information_material(self):
        print(f"{self.morf}")

class Plastic(Steklo):

    def __init__(self, strength, morf, color, form, open):
        super().__init__(strength, morf, color, form)
        self.open = open

class Window(Plastic):
    def __init__(self, strength, morf, color, form, obem, sharnir):
        super().__init__(strength, morf, color, form, obem)
        self.sharnir = sharnir

class Butilka(Steklo):
    def __init__(self, strength, morf, color, form, obem):
        super().__init__(strength, morf, color, form)
        self.obem = obem

class Juice(Butilka):
    def __init__(self, strength, morf, color, form, obem, naturale):
        super().__init__(strength, morf, color, form, obem)
        self.naturale = naturale

class Cup(Steklo):
    def __init__(self, strength, morf, color, form, ruchka):
        super().__init__(strength, morf, color, form)
        self.ruchka = ruchka
class Termos(Cup):
    def __init__(self, strength, morf, color, form, ruchka, temp):
        super().__init__(strength, morf, color, form, ruchka)
        self.temp = temp
class Glasses(Steklo):
    def __init__(self, strength, morf, color, form, medicakl):
        super().__init__(strength, morf, color, form)
        self.medicakl = medicakl
class Mode_glasses(Glasses):
    def __init__(self, strength, morf, color, form, medicakl, oprava):
        super().__init__(strength, morf, color, form, medicakl)
        self.oprava = oprava
class Door(Steklo):
    def __init__(self, strength, morf, color, form, ramka):
        super().__init__(strength, morf, color, form)
        self.ramka = ramka
class Opened(Door):
    def __init__(self, strength, morf, color, form, ramka, open):
        super().__init__(strength, morf, color, form, ramka)
        self.open = open