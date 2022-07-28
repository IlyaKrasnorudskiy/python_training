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
