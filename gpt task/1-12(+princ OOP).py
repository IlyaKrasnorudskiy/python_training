class Product:
    def __init__(self, id, name, cost):
        self.__id = id
        self.__name = name
        self.__cost = cost
        self.__cost = self.check_cost()

    def check_cost(self):
        if self.__cost < 0:
            raise ValueError('Цена не может быть меньше нуля!')
        else:
            return self.__cost

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.__cost == other.__cost
        else:
            return False

class WareHouse:
    stock = {
        1:5,
        2:3
    }
    @classmethod
    def is_avai(cls, product_id, q = 1):
        return cls.stock.get(product_id, 0) >= q

class Cart:
    def __init__(self):
        self.__products = []
        self.__count = 0

    def add_prod(self, obj_product, count = 1):
        self.__products.append(obj_product)
        self.__count += count

    def del_prod(self, obj_product, count = 1):
        self.__products.remove(obj_product)
        self.__count -= count



num1 = Product('1', 'computer', 1000)
print(num1.__dict__)
num2 = Product('12', 'mobile phone', 500)
print(num1 == num2)
b = Cart()
b.add_prod(num1, 5000)
b.add_prod(num2, 5000)
b.del_prod(num2, 3000)
print(b.__dict__)