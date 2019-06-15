"""
Основы ООП - конструктор, наследование, перегрузка, полиморфизм, инкапсуляция
"""


class Human:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name='Undefined'):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Human: {self.first_name} {self.last_name}'


class User(Human):
    __passport: str = "1234 123123"

    def hello(self):
        print(f'Hello, {self.first_name}!')


john = User('John', 'Doe')
john.hello()
print(john)

print(john._User__passport)
