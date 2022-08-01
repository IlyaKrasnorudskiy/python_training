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

