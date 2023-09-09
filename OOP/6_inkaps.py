class Point:
    color = 'red'
    circle = 2

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def __init__(self, x = 0, y = 0):
        if self.__check_value(x) and self.__check_value(y):
            print('вызов __init__')
            self.__x = x
            self.__y = y

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("ONLY NUMBER!")

    def get_coords(self):
        return self.__x, self.__y

pt = Point(20, 30)
pt.set_coords(12, 23.5)
print(pt.get_coords())
print(dir(pt))
