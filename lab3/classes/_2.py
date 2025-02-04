class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

sha = Shape()
print(sha.area())
square = Square(5)
print("Area: ", square.area())