def clear_number(s):
    k = ''
    for i in s:
       if i.isdigit():
           k += i
    return k
s = "+7(123)546-65-92"
print(clear_number(s))