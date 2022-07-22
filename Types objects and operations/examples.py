s = "fgassdadssdsdasdasdhelloasdasdasdasdasd"
for i in s:
    if "hello" in s:
        print(True)
        break

print("Срез строки [1:6:2] ", s[1:6:2])

l  = ["hello", 12, 23.2, "bye"]
print(l[:-1])
#конкатенация
l += [1,2,3]
print(l*2)
print(l.reverse())
#array inclusions
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
#Получим второй столбец с помощью спискового включения
col2 = [row[1] for row in matrix]
print(col2)
#руками
col2 = []
for i in range(0, len(matrix)):
    col2.append(matrix[i][1])
print(col2)
#собираем диагональ
diag = [matrix[i][i] for i in [0,1,2]]
print(diag)
#Словари

D = {'food': "Spam", 'quantity':4, 'color': 'Pink'}
print(D['food'])
D['quantity']+=1
print(D)
D['test'] = 3, 4, 5
print(D)
#другой способ создания словаря
D1 = dict(name = 'Ilya', age = '19')
print(D1)
#Связывание словарей
D_double = dict(zip(D, D1))
print(D_double)
#Больше информации
rec = {'name': {'first': 'Ilya', 'last':'Valera'},
       'jobs': ['dev', 'mgr'],
       'age': 19.5}
print(rec['name'])
print(rec['name']['last'])
rec['jobs'].append('jun')
print(rec['jobs'][0])
#очистка области памятиhttps:
#rec = 0
#недостающие ключи : проверки if
if not 'f' in rec:
    print('missing')
value = rec.get('x', 0)
print(value)
#Сортировка ключей
ks = list(rec.keys())
print(ks)
ks.sort()
print(ks)
for key in ks:
    print(key, '=>', rec[key])
#Кортежи
T = (1, 2, 3, 4)
T += (5, 6)
print(T[5])
T1 = 'spam', 3.97, [1,2,3]
print(T1[2][0])
#множества
x = set('spam')
y = {'h', 'a', 'm'}
print(x&y)
print(x|y)
print(x-y)
print(x>y)
#фильтрация дубликатa
mas = [1,2,3,1,2,1,3,2,4,4]
mnojestvo = set(mas)
print(mnojestvo)

#Булевские значения
print(1>2, 2>3)



#type object
l = []
t = ()
print(type(l))
print(type(type(t)))
#type class OOP
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0+percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())
sue.giveRaise(.10)
print(sue.pay)
