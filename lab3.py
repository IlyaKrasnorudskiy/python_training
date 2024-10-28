class VendingMachine:
    def __init__(self):
        self.state = 0  # Начальное состояние
        self.product_price = 300  # Стоимость товара

    def insert_money(self, amount):
        # Допустимые купюры
        if amount not in [100, 200, 500]:
            print(f"Купюра номиналом {amount} рублей не принимается.")
            return

        self.state += amount
        print(f"Вы внесли {amount} рублей. Текущая сумма: {self.state} рублей.")

        # Проверка на возможность покупки
        if self.state >= self.product_price:
            self.dispense_product()

    def dispense_product(self):
        print("Товар выдан.")
        change = self.state - self.product_price
        if change > 0:
            print(f"Ваша сдача: {change} рублей.")
        self.reset()

    def reset(self):
        print("Автомат сброшен. Можно вносить новую сумму.")
        self.state = 0


vending_machine = VendingMachine()

print(
    f"Добро пожаловать! Стоимость товара {vending_machine.product_price} рублей. Вносите купюры номиналом 100, 200 или 500 рублей.")
print("Для завершения работы введите 'stop'.")
while True:
    user_input = input("Внесите купюру: ")

    if user_input.lower() == 'stop':
        print("Работа завершена.")
        break

    try:
        amount = int(user_input)
        vending_machine.insert_money(amount)
    except ValueError:
        print("Пожалуйста, введите число или 'stop' для завершения.")