class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def show(self):
        print(f"Abscissa (x): {self.a}")
        print(f"Ordinate (y): {self.b}")
    
    def move(self):
        self.a = int(input("Change abscissa (x): "))
        self.b = int(input("Change ordinate (y): "))

    def dist(self):
        self.box1 = abs(self.a - int(input("Abcissa (x) for distance: ")))
        self.box2 = abs(self.b - int(input("Ordinate (y) for distance: ")))
        print(f"New abscissa (x): {self.box1}\nNew ordinate (y): {self.box2}")

point = Point(int(input()), int(input()))
point.show()
point.move()
point.show()
point.dist()