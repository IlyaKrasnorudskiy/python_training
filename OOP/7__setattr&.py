class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def set_coords(self, x, y):
        if self.MIN_COORD > x:
            print('больше')
            self.x = x
            self.y = y

    def get_coords(self, x):
        return (self.x, self.y)
    @classmethod
    def set_bound(cls, lexa):
        cls.MIN_COORD = lexa

    def __getattribute__(self, item):
        if item == "z":
            raise ValueError("доступ запрещен")
        else:
            print("__")
            return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('недопуст. имя атр.')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("get_attr"+item)
        return False

    def __delattr__(self, item):
        print("del_attr" + item)
        object.__delattr__(self, item)

pt = Point()
pt.set_coords(-10,20)
pt.set_bound(20)
print(pt.__dict__)
print(Point.MIN_COORD)
a = pt.y
print(a)
#pt.z = 3
print(pt.__dict__)
print(pt.zxc)
del pt.x
print(pt.__dict__)