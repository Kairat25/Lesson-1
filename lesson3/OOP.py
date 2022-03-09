class Builder:

    def can_build(self):
        print("I can build!")

class Doctor:

    def can_help(self):
        print("I can help!")

class Programmer:

    def can_write_code(self):
        print("I can write code on Pythone")

    def can_build(self):
        print("I am a programmer but i can build!")

class Person(Doctor, Programmer, Builder):
    pass

jack = Person()
# jack.can_write_code()
jack.can_build()
# print(Person.__mro__)