import abstrac

class Car(abstrac.AbstractTransport):


    def __init__(self, tiyle, model, color, speed):
        super().__init__(tiyle, model, color)
        self.speed = speed


class Airplane(abstrac.AbstractTransport):


    def __init__(self, tiyle, model, color, speed):
        super(Airplane, self).__init__(tiyle, model, color)
        self.speed = speed