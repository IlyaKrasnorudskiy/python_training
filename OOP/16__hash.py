print(hash(123))
print(hash("Python"))
print(hash((1, 2, 3)))
#для списков нельзя вычислить хэш

d = {}

d[5] = 5
d['python'] = 123
#для ключей словаря только хешируемые объекты(неизменяемые)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1,2)
p2 = Point(1,2)
print(hash(p1), hash(p2))
print(p1 == p2)
d = {}
d[p1] = 1
d[p2] = 2
print(d)