class Point:
    color = 'red'
    circle = 2

    def __init__(self, x = 0, y = 0):
        print('вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра" + str(self))
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point(1, 5)
print(pt.__dict__)
print(pt.x , pt.y)
pt2 = Point()
print(pt2.__dict__)