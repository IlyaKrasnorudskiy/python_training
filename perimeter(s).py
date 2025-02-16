s = '345x11'
a = ''
b = ''
flag = 0
for i in s:
    if i == "x":
        flag = 1
    if i.isdigit() and flag == 0:
        a += i
        flag = 0
    if flag == 1 and i != "x":
        b += i
