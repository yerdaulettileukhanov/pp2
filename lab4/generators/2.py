class Even:
    def __init__(self, n):
        self.stop = n
    
    def __iter__(self):
        self.start = 0
        return self
    
    def __next__(self):
        self.start += 2
        if self.start <= self.stop:
            return self.start
        else:
            raise StopIteration

a = Even(20)
b = iter(a)

for i in b:
    print(i, end=", ")