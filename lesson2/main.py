class Animal:
    def __init__(self, name, type, color, voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)



class Dog(Animal):
    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)

class Cat(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)




rex = Dog(
    'rex', 'Domestic', 'Blue', 'gaf gaf!')

barsik = Cat('Barsik', 'Domestic', 'White-Black', 'miauu')

rex.voice()
barsik.voice()


class Horse(Animal):

    def __init__(self, name, type, color, voiceText, speed, weight):
        super().__init__(name, type, color, voiceText)
        self.speed = speed
        self.weight = weight

    def voice(self):
        print(f'{self.name}: {self.voiceText}')

mustang = Horse('Mustang', 'Domestic', 'brown', 'kukariku', 30, 250)
mustang.voice()


