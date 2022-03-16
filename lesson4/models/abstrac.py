
# """   Base Class Transport for Cars   """


class AbstractTransport:
    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color =color
# """
# Method start engine
# return str() in terminal
# """

    def start_engine(self):
        print(f"On {self.title}, {self.model}, {self.color} engine strarted! ")