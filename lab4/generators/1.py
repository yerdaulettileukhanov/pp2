class Squares:
    def __init__(self, n):
        self.stop = n
    
    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start != self.stop:
            self.start += 1
            return self.start ** 2
        else:
            raise StopIteration

a = Squares(4)
it1 = iter(a)

for i in it1:
    print(i)