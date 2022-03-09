class Transport:

    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"On {self.title} {self.model} {self.color}")

class Car(Transport):


    _current_speed = 0
    def __init__(self, title, model, color, maxSpeed, speed):
        super().__init__(title, model, color)
        self.maxSpeed = maxSpeed
        self.speed = speed


    def _get_current_speed(self):
        print(f'{self.title} {self.model} speed: {self._current_speed}')


    def gas(self):
        if self._current_speed < self.maxSpeed:
            self._current_speed += self.speed
            self._get_current_speed()
        else:
            print('CHECK ON!')

    def break_speed(self):
            if self._current_speed - self.speed < 0:
                print("Car stoped!")
            else:
                self._current_speed -= self.speed
                self._get_current_speed()



bmw = Car('BMW', 'M8', 'Brooklyn Green', 460, 40)
bmw.gas()
bmw.gas()
bmw.gas()
bmw.gas()
bmw.gas()

bmw.break_speed()
bmw.break_speed()