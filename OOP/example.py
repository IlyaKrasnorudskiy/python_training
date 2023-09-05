# Базовый класс Vehicle (транспортное средство)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "Двигатель запущен"

    def stop_engine(self):
        return "Двигатель остановлен"


# Класс Car наследует от класса Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        return "Би-би!"


# Класс Motorcycle наследует от класса Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def honk(self):
        return "Гудок мотоцикла!"



car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Roadster", 2019, False)

print(car.start_engine())
print(car.honk())
print(motorcycle.start_engine())
print(motorcycle.honk())

D =

