#Ex1
class Str:
    def getString(self):
        self.box = input()
    def printString(self):
        print(self.box)

a = Str()
a.getString()
a.printString()