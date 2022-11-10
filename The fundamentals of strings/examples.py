string = 'abcdefg'
string = string[:2:-1]
print(string)
lst = [1,2,3,1,11,12]
maxs = max(lst)
mins = min(lst)
arr = []
arr.append(mins)
arr.append(maxs)
print(arr)
num = 70304
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

print(mas_categories_str)

s = 1.08
s = (s * 1000*100) / (3600)
print(int(s))

#коды символов
print(ord('s'))
print(chr(115))
s = '5'
s = chr(ord(s)+1)
print(s)

