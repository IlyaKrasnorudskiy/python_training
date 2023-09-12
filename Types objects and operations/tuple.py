a = 1, 2
print(a)
a = (1, 2, 3)
print(a)
x , y = ["hello", "python"]
print(x, y)
a, b = 'ra'
print(a, b)
a = (1, 2, 3)
print(len(a))
print(a[1])
print(a[1:2])
b = a[:]
print(id(a), id(b))
print(hash(a), hash(b))

"""
a = [1, 2, 3]
b = a[:]
print(id(a), id(b))
"""
d = {}
d[a] = "кортеж"
print(d)
lst = [1, 2, 3] 
print(lst.__sizeof__())
print(a.__sizeof__())

b = tuple()
b += (1,)
print(b)