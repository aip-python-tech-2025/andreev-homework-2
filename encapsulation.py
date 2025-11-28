class Transaction:
    def __init__(self, amount, sender=None, recipient=None):
        self.__sender = sender
        self.__recipient = recipient
        self.__amount = amount

    def __repr__(self):
        return f'{self.__sender} -> {self.__recipient} with amount = {self.__amount}'

class Client:
    def __init__(self, name, initial_balance):
        self._name = name
        self._balance = initial_balance
        self._transactions = []

    def __str__(self):
        return f'{self._name} with balance = {self._balance}'

    def transfer(self, recipient, amount):
        if self._balance >= amount:
            recipient._balance += amount
            self._balance -= amount
            self._transactions.append(Transaction(amount, self, recipient))
            recipient._transactions.append(Transaction(amount, recipient, self))

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(Transaction(amount, None, self))

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self._transactions.append(Transaction(amount, self, None))

    def pay(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self._transactions.append(Transaction(amount, self, None))

    # Функция-геттер
    def get_name(self):
        return self._name

    # Функция-сеттер
    def change_name(self, new_name):
        bad_words = ['дурак']
        if new_name not in bad_words:
            self._name = new_name

    # Геттер
    @property
    def name(self):
        return self._name

    # Сеттер
    @name.setter
    def name(self, new_name):
        self.change_name(new_name)


class VipClient(Client):
    def __init__(self, name, initial_balance):
        super().__init__(name, initial_balance)
        self.__bonuses = 0

    def pay(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self.__bonuses += int(amount * 0.15)
            self._transactions.append(Transaction(amount, self, None))

    def __str__(self):
        return f'{self._name} with balance = {self._balance} and bonuses = {self.__bonuses}'


alice = Client(name='Alice', initial_balance=1000)
bob = Client(name='Bob', initial_balance=2000)
charlie = VipClient(name='Charlie', initial_balance=3000)

for client in alice, bob, charlie:
    client.pay(100)
    print(client)

# alice.pay(100)
# bob.pay(100)
# charlie.pay(100)

bob.transfer(alice, 100)
charlie.transfer(alice, 100)
charlie.transfer(bob, 150)

# charlie._Client__balance = 10000

print(alice)
print(bob)
print(charlie)

charlie.name += ' Smith'
print(charlie.name)

print(alice.name)
alice.name = 'Алиса'
print(alice.name)

print(alice._transactions)
print(bob._transactions)
print(charlie._transactions)
