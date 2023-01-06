file = open("numbers.txt", "r")
numbers = file.readlines()
multiplication = 1
for i in numbers:
    multiplication *= float(i)
print(multiplication)