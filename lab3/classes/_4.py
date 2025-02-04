import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: ", self.x, "and", self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, other):
        print(round(math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2),2))

po = Point(0, 0)
p1 = Point(1 ,64)
po.move(6 , 5)
po.show()
po.dist(p1)