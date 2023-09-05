class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целой")
    def __set_name__(self, Point3D, name):
        self.name = "_" + name
    def __get__(self, instance, Point3D):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    '''
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
         self.verify_coord(x)
         self._x = x

    @property
    def y(self):
        return self._x

    @y.setter
    def y(self, y):
        self.verify_coord(y)
        self._x = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self.verify_coord(z)
        self._z = z

    '''


p = Point3D(1,2,3)
print(p.__dict__)
print(p._x)
p.y = 10
print(p.__dict__)