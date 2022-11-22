res = [c*4 for c in 'SPAM']
print(res)
#файлы
myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.close()
myfile = open('myfile.txt', 'r')
print(myfile.readline())
data = open('data.bin', 'rb').read()

print(data)
#JSON
name = dict(first = 'Bob', last = 'Smith')
rec = dict(name = name, job =['dev', 'mgr'], age = 40.5)
print(name)
print(rec)

import json
print(json.dumps(rec))

s = json.dumps(rec)
print(s)

O = json.loads(s)
print(O)
L = [None]*100
print(L)
#Можно использовать на проверке занятости
print(bool('2'))

#Проверка типов
l = [1]
print(type(l))
print(isinstance(l,list))

