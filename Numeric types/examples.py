from decimal import Decimal
from fractions import Fraction
#comlex number
print(1j * 1J)
print(2+1j*3)
#Системы счисления
#8
print(0o1, 0o20, 0o377)
a = oct(64)
print(a)
#16
print(0x01, 0x10, 0xFF)
a = hex(64)
print(a)
#2
print(0b1, 0b10000, 0b11111111)
a = bin(64)
print(a)
#eval функция
test = eval(a) #line 15
print(test)
#Побитовые операции
x = 0b0001
print(x<<2) #сдвиг влево
#основы десят чисел
print(0.1+0.1+0.1-0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
#дроби
x = Fraction(1, 3)
print(x)
x+= 0.1
print(x)
#множества

number = 999
number_as_string = str(number)
print(int(number_as_string[1]) + 2)
num = 0
s = ''
num_str = str(num)
for i in num_str:
    s += str(int(i)*int(i))
print(s)
a = str(hex(255))
a = a[2::].upper()
print(hex(0))