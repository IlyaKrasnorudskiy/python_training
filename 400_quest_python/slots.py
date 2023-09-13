class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


test1 = Person('Ilya', 20)
#строчка ниже вызовет исключение AttributeError
#test1.address = 'hello world'
