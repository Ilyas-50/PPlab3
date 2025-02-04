from _2 import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def calculate(self):
        return self.length * self.width

figure = Rectangle(8, 9)
print(figure.calculate())