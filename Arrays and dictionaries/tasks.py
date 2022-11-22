'''
Предугадывание операций
'''
print(2**16)
print(2/5.2/5.0)
print("spams"+"eggs")
S="ham"
print("eggs"+S)
print(S*5)
#Посмотреть больше об этом
print("green %s and %s" % ("eggs", S))
print('green {0} and {1}'.format('eggs', S))
#Больше
a = ('x',)[0]
print(a)
b = ('x','y','z')[1]
print(b)
L = [1,2,3]+[4,5,6]
print(L,L[:],L[:0],L[-2],L[-2:])
CORT = (L)[2:4]
print(CORT)
print([L[2], L[3]])
L.reverse()
print(L)
L.sort()
print(L)
#Взятие индекса по значению элемента
print(L.index(4))
dict = {'a':1, 'b':2}['b']
print(dict)
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
print(D)
print(D['x'] + D['w'])
#Не угадал
D[('x',2,3)] = 4
print(D)
print(list(D.keys()))
print(list(D.values()))
print((1,2,3) in D)
print([[]])
print(["",[],(),{},None])
x = 'spam'
y = 'eggs'
x, y = y, x
print(x, y)