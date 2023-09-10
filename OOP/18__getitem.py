class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if item > len(self.marks):
            raise IndexError("Такого индекса нет!")
        else:
            return self.marks[item]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if not(key > len(self.marks)):
                self.marks[key] = value
            else:
                raise IndexError("Такого индекса нет! ")
        else:
            raise TypeError("Вы ввели неверный тип данных !")

    def __delitem__(self, key):
        self.marks.pop(key)

s1 = Student("Илья", [5, 5, 3, 2, 5])
s1[3] = 12
del s1[2]
print(s1.marks)
