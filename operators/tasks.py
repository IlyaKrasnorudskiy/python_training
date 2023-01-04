#задачи из Практикум по алгоритмизации и программированию на Python Иван Хахаев, 2009
'''
Определить,   является ли введённая строка палиндромом
(«перевёртышем») типа ABBA, kazak и пр.
'''
def palindrom(line):
    arr1 = []
    for i in range(0, len(line)):
        if line[len(line) - i - 1] == line[i]:
           arr1.append(line[i])
           print(arr1)
           if arr1 == list(line):
               return True
    return False
print(palindrom('kazak'))
print(palindrom('12332'))

'''
Дан одномерный массив числовых значений, насчитывающий N элементов.
Определить образуют ли элементы массива,   расположенные перед первым
отрицательным элементом, возрастающую последовательность
'''
n = int(input("n = "))
arr = []
flag = 0
for i in range(0, n):
    a = int(input("value = "))
    arr.append(a)
for i in range(0, len(arr)-1):
    if arr[i] < 0:
        line = arr[i+1:n]
        new_arr = list(line)
k = 1
for i in range(0,len(new_arr)-1):
    if new_arr[i] < new_arr[i+1]:
        k += 1
        if k == len(new_arr) :
            print("Образует")

