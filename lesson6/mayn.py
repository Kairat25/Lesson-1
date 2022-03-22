class Indent

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def test(self):
        print(self.attr1, self.attr2)


indent = Indent('attr1', 'attr2')
