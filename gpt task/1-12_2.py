class ManageScore:
    scores = []
    def __set_name__(self, BankAccount, name):
            self.name = "__" + name

    def __get__(self, instance, BankAccount):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value in self.scores:
            raise ValueError("Такой id уже есть!")
        else:
            self.scores.append(value)
            instance.__dict__[self.name] = value

class BankAccount:
    account_id = ManageScore()
    holder_name = ManageScore()
    balance = ManageScore()
    def __init__(self, id, h_m, number):
        self.account_id = id
        self.holder_name = h_m
        self.balance = number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств для вывода!")

    def __str__(self):
        return f'account_id : {self.account_id}, holder_name:{self.holder_name}, balance: {self.balance}  '

sc = BankAccount('1111', 'Il2ya', 30000)
print(sc)
print(sc.balance)
sc.deposit(5000)
print(sc.balance)
sc.withdraw(2500)
print(sc.balance)
sc2 = BankAccount('12311', 'Ily2a', 300002)
print(sc2)


