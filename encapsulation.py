class Client:
    def __init__(self, name, initial_balance):
        self.__name = name
        self.__balance = initial_balance

    def __str__(self):
        return f'{self.__name} with balance = {self.__balance}'

    def transfer(self, recipient, amount):
        if self.__balance >= amount:
            recipient.__balance += amount
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount

    # Функция-геттер
    def get_name(self):
        return self.__name

    # Функция-сеттер
    def change_name(self, new_name):
        bad_words = ['дурак']
        if new_name not in bad_words:
            self.__name = new_name

    # Геттер
    @property
    def name(self):
        return self.__name

    # Сеттер
    @name.setter
    def name(self, new_name):
        self.change_name(new_name)


class VipClient(Client):
    pass


alice = Client(name='Alice', initial_balance=100)
bob = Client(name='Bob', initial_balance=200)
charlie = VipClient(name='Charlie', initial_balance=300)

bob.transfer(alice, 100)
charlie.transfer(alice, 100)
charlie.transfer(bob, 150)

# charlie._Client__balance = 10000

print(alice)
print(bob)
print(charlie)

charlie.name += ' Smith'
# charlie.change_name(charlie.get_name() + ' Smith')
print(charlie.name)

print(alice.name)
alice.name = 'Алиса'
print(alice.name)