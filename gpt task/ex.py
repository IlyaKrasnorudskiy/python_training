class Animal:
    def __init__(self, name, age, genus):
        self.__name = name
        self.__age = age
        self.__genus = genus

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def genus(self):
        return self.__genus

    make_sounds = {
        'Лев': "РРР!",
        'Попугай': "Чик-чик",
        'Змея': "ШШШш!"
    }
    genus_mas = ['Кошачьи', 'Птицы', 'Млекопитающие']

    def song(self):
        if self.__name in Animal.make_sounds.keys():
            return Animal.make_sounds[self.__name]

    def __str__(self):
        return f"Имя : {self.__name}, Возраст : {self.__age}, Вид : {self.__genus}, Голос : {self.song()}"

class Enclosure(Animal):
    def __init__(self, number_enc, genus_enc):
        self._number_enc = number_enc
        self._genus_enc = genus_enc
        self._mas_animal = []

    def __str__(self):
        animals_str = ''
        for animal in self._mas_animal:
                animals_str += ' ' + str(animal)
        return f"Номер вольера: {self._number_enc}, Семейство вольера: {self._genus_enc}, Список животных: {animals_str} "

    def add_animal(self, obj_animal):
        if not isinstance(obj_animal, Animal):
            raise TypeError("Передайте объект с данными о животном!")
        else:
            if not(obj_animal.genus in Animal.genus_mas):
                raise ValueError("Такого семейства в вольере нет!")
            else:
                self._mas_animal.append(obj_animal)


class Zoo(Enclosure):
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self._count_enc = 0
        self._mas_enc =[]

    def add_vol(self, obj_vol):
        if not isinstance(obj_vol, Enclosure):
            raise TypeError("Вольер не подходит!")
        else:
            self._count_enc += 1
            self._mas_enc.append(obj_vol)

    def __str__(self):
        return f"Название Зоопарка: {self.name_zoo}, Количество вольеров:{self._count_enc}"

    def info(self):
        info = ''
        for enc in self._mas_enc:
            info += str(enc) + '\n'
        return info



Lion = Animal('Лев', '8', 'Кошачьи')
Tiger = Animal('Тигр', '2', 'Кошачьи')
vol1 = Enclosure('1', 'Кошачьи')
print(Lion)
vol1.add_animal(Lion)
vol1.add_animal(Tiger)

print(vol1)
Paradel = Zoo('Paradel')
Paradel.add_vol(vol1)
print(Paradel)
print(Paradel.info)