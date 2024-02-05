class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

a = Rectangle(12, 2)
a.area()