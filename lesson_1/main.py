class Car:

    _currentSpeed = 0

    def __init__(self, title, model, color, max_speed, speed):
        print(title, model, color)
        self.title = title
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.speed = speed




    def start_engine(self):
        print(f'On {self.title} {self.model} engine starterd!')


    def gas(self):
        if self._currentSpeed >= self.max_speed:
            print('Check ON!')
        else:
            self._currentSpeed += self.speed
            print(self._currentSpeed)


        """Instance"""
bmw = Car('BMW', 'e38', 'blue', 360, 20)
bmw.start_engine()
bmw.gas()
mercedes = Car('MERCEDES', '220', 'black', 340, 10)
mercedes.start_engine()


# print(
#     f"Title: {bmw.title}\nModel: {bmw.model}\nColor: {bmw.color}"
# )
