def multiply(a, b):
    return a * b

def boolean_to_string(b):
    return str(b)

def summation(num):
    sum = 0
    for i in range(1, num+1):
        sum+=i
    return sum


def minimum(arr):
    arr.sort()
    return arr[0]
def maximum(arr):
    arr.sort()
    return arr[-1]

def no_space(x):
    for i in x:
        if i == ' ':
            x = x.replace(' ',"")
    return x

def solution(string):
    return string[::-1]

def number_to_string(num):
    return str(num)

def sum_array(a):
    sum = 0
    for i in range(0, len(a)):
        if a[i]!=0:
            sum+=a[i]
    return sum

def maps(a):
    for i in range(0, len(a)):
        a[i] *= 2
    return a

def digitize(n):
    n = str(n)
    k = len(n)
    n = n[::-1]
    l = []
    for i in range(0, k):
        l.append(int(n[i]))
    return l

def find_smallest_int(arr):
    return min(arr)

def remove_char(s):
    s = s.replace(s[0], '', 1)
    s = s.replace(s[-1], '', 1)
    return s

def remove_char(s):
    s = s[1::]
    s = s[:len(s)-1:]
    return s

def sum_array(arr):
    return 0 if arr == None  or len(arr) < 3 else sum(arr) - (max(arr) + min(arr))

def repeat_str(repeat, string):
    return string*repeat

num = 0
def descending_order(num):
    while True:
        if num == 0:
            return num
        num = str(num)
        arr = []
        stroka = ''
        for i in num:
            arr.append(int(i))
        arr.sort()
        for i in range(-1, -len(arr)-1, -1):
            stroka += str(arr[i])
        stroka = int(stroka)
        break
    return stroka
print(descending_order(151))
s = ['2','2','1']
s = ''.join(s)
print(int(s)+1)

a = 6
b = 2
c = bin(a+b)


def add_binary(a, b):
    x = a + b
    s = ''
    while x != 0:
        s += str(x % 2)
        x = x // 2
    return s[::-1]
print(2.5/100)

def nb_year(p0, percent, aug, p):
    k = 0
    while p0 < p:
        p0 = p0 + p0*percent/100 + aug
        k+=1
    return k

def accum(s):
    new_str = ''
    for i in range(0, len(s)):
        new_str += s[i].capitalize()
        new_str += s[i].lower() * i
        if i != len(s)-1:
            new_str += '-'
    return new_str
print(accum('ZFasdad'))
a = '+'
val1= '1'
val2= '2'
str = str(val1)+a+str(val2)
print(str)




def century(year):
    if year%10>0 or year//10%10>0:
        return year//100 + 1
    else:
        return year//100

a=3
b=2
if type(a) == type(b):
    print('good')


def filter_list(l):
    help = 2
    for a in l:
        if type(a) != type(help):
            l.remove(a)
    return l

print(filter_list([1, 2,'b','c']))


#МУТАЦИЯ
def remove_smallest(numbers):
    min = 100000000
    member = 0
    for i in range(0, len(numbers)):
        if min > numbers[i]:
            min = numbers[i]
            member = i
    if len(numbers) > 0:
        numbers.pop(member)
    return numbers

def find_average(numbers):
    sum = 0
    for a in numbers:
        sum+=a
    return sum/len(numbers)

#
def high_and_low(numbers):
    max = 0
    min = 9999
    for i in numbers:
        if i != ' ' or i != '-':
            if min > int(i):
                min = int(i)
            if max < int(i):
                max = int(i)
    string = str(max) + ' ' + str(min)
    return string

