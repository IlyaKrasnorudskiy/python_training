class Point:
    "Класс для предст. точек"
    color = 'red'
    circle = 2

a = Point()
print(a.color)
a.color = 'green'
print(getattr(a, 'color'))
b = Point()
print(hasattr(b, 'circle'))
b.color = 'blue'
print(b.__dict__)
setattr(Point, 'circle', 3)
print(a.circle)
delattr(b, 'color')
print(b.__dict__)
print(b.__doc__)