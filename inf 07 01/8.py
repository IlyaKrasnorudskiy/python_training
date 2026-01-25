import turtle as t # Подключим модуль черепашка
k = 25 # коэффициент для настраивания более удобного масштаба
t.left(90)
t.speed(0)
for i in range(4): # пропишем алгоритм построения фигуры по условию
    t.forward(10 * k)
    t.right(60)
    t.forward(10 * k)
    t.right(120)
t.up()
t.speed(10) # Увеличим скорость черепашки
for x in range(-10, 15): # Алгоритм построения точек
    for y in range(0, 20):
        t.goto(x * k, y * k)
        t.dot(3) # точки размером 4 пикселя
t.done()