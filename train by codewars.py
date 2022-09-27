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


def find_short(s):
    k = 0
    l = []
    s+=' '
    for i in s:
        if i != ' ':
            k+=1
        else:
            l.append(k)
            k = 0
    return min(l)
print(find_short("bitcoin take over the world maybe who knows perhaps"))

def count_by(x, n):
    l = []
    k = x
    for i in range(1, n+1):
        l.append(x)
        x += k
    return l

print(count_by(1, 5))

def bmi(weight, height):
    bmi = weight/height**2
    if bmi <= 18.5:
        return "Underweight"

    if bmi <= 25.0:
        return "Normal"

    if bmi <= 30.0:
        return "Overweight"

    if bmi > 30:
        return "Obese"
    return bmi

def dna_to_rna(dna):
    return dna.replace("T", "U")

def double_char(s):
    string = ''
    for a in s:
        string += a*2
    return string


def spin_words(sentence):
    sentence += ' '
    test = ''
    l = []
    string = ''
    for i in range(0,len(sentence)):
        if sentence[i] != ' ':
            test+=sentence[i]
        else:
            l.append(test)
            test = ''
    print(l)
    for i in range(0, len(l)):
        if len(l[i]) >= 5:
            l[i] = l[i][::-1]
        string += l[i]
        if l[i] != l[-1]:
            string += ' '
    return string
print(spin_words("Hey fellow warriors"))


def camel_case(string):
    l = []
    string+=' '
    test = ''
    st = ''
    for i in range(0,len(string)):
        if string[i] != ' ':
            test+=string[i]
        else:
            l.append(test)
            test =''
    for a in l:
        st += a.capitalize()
    return st
print(camel_case("camel case method"))

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

def opposite(number):
    return -number

def positive_sum(arr):
    sum = 0
    for a in arr:
        if a > 0:
            sum += a
    if sum == 0:
        return 0
    return sum

def set_alarm(employed, vacation):
    if employed > vacation:
        return True
    else:
        return False

def get_sum(a, b):
    if a == b:
        return a
    else:
        return a + b

def make_upper_case(s):
    return s.upper()

def smash(words):
    s = ''
    k = 0
    for i in words:
        if k == 0:
            s += i
            k+=1
        else:
            s+=' ' + i
    return(s)

def divisors(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0:
            k+=1
    return k
def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i*i
    return sum
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1]* matrix[1][0])
    if len(matrix) == 3:
        return (matrix[0][0]*matrix[1][1]*matrix[2][2])+(matrix[0][1]*matrix[1][2]*matrix[2][0])+(matrix[1][0]*matrix[2][1]*matrix[0][2])-((matrix[0][2]*matrix[1][1]*matrix[2][0])+(matrix[1][0]*matrix[0][1]*matrix[2][2])+(matrix[1][2]*matrix[2][1]*matrix[0][0]))

    def translate(a):
        base = 16
        s = ''
        while a != 0:
            s += str(a % base)
            a = a // base
            return str(s.reverse())

    def rgb(r, g, b):
        return translate(r) + translate(g) + translate(b)

    print(rgb(255,255,255))


def abbrev_name(name):
    first = name[0].capitalize()
    for i in range(0,len(name)):
        if name[i] == ' ':
            last = name[i+1].upper()
    return str(first) + '.' + str(last)

def string_to_array(s):
    if s == "":
        mas = []
        mas.append(s)
        return mas
    return s.split()

def fake_bin(x):
    for i in x:
        if int(i) < 5:
            x = x.replace(i, '0', 1)
        else:
            x = x.replace(i, '1', 1)
    return x
print(fake_bin("45385593107843568"))