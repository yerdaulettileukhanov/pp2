class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

a = Square(3)
a.area()