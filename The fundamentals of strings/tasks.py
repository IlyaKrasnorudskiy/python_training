def duplicate_count(text):
    text = text.upper()
    print(text)
    count = 0
    for i in text:
        if text.count(i) > 1:
            count+=1
            text = text.replace(i, '')
            print(text)
    return count
print(duplicate_count('aabbcc'))
#Солидно



def unique_in_order(iterable):
    l = []
    for i in range(len(iterable)-1 ):
        buf = iterable[i]
        if buf != iterable[i+1]:
            l.append(buf)
    l.append(iterable[-1])
    return l
print(unique_in_order(('AAAABBBCCDAABB  B')))


def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


def solution(string, ending):
    string = string[:2:-1]
    if ending in string:
        return True
    else:
        return False

def min_max(lst):
    maxs = max(lst)
    mins = min(lst)
    arr = []
    arr.append(mins)
    arr.append(maxs)
    return arr

def expanded_form(num):
    num = str(num)
    mas_categories = []
    k = 0
    for i in num:
        k+=1
        if i == '0':
            continue
        number = i + (len(num)-k) * '0'
        print(number)
        mas_categories.append(number)
    mas_categories_str = " + ".join(mas_categories)
    return mas_categories_str

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'

def cockroach_speed(s):
    return int((s * 1000*100) / (3600))

def litres(time):
    return int(time*0.5)


