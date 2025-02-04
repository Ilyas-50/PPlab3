class First():
    def __init__(self, string):
        self.string = string

    def getString(self):
        print(self.string)

    def printString(self):
        print(self.string.upper())

p1 = First("strExample")
p1.getString()
p1.printString()




