from turtle import *

tracer(0)

# Коэффициент увеличения
k = 20

left(90)
for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)

# Поднять хвост
penup()

forward(5 * k)
right(90)
forward(7 * k)
left(90)

# Опустить хвост
pendown()

for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)

# Поднимаем перо, чтобы нарисовать координатную сетку
penup()
for x in range(-10, 20):
    for y in range(-10, 20):
        setpos(x * k, y * k)
        dot(4, 'red')