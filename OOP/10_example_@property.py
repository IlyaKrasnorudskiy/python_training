from string import ascii_letters


class Person:
    S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбю-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, age, serial, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.age = age
        self.serial = serial
        self.weight = weight


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("фио-строка!")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("неверный формат!")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('должен хотя бы один символ быть!')
            if len(s.strip(letters)) != 0:
                raise TypeError('в фио только буквы и дефис!')

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 100:
            raise TypeError("возраст целое число!(14..100)")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("вес должен быть от 20 кг и вещ.числ.!")

    @classmethod
    def verify_serial(cls, serial):
        if type(serial) != str:
            raise TypeError("серия - строка!")

        s = serial.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('неверный формат паспорта!')

        for p in s:
            if not p.isdigit():
                raise TypeError('в паспорте не должно быть лишних символов!')

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def serial(self):
        return self.__serial

    @serial.setter
    def serial(self, serial):
        self.verify_serial(serial)
        self.__serial = serial

p = Person('Краснорудский Илья Викторович', 20, '1111 222222', 90.4)

print(p.fio)
p.age = 15
print(p.age)
print(p.serial)
print(p.__dict__)