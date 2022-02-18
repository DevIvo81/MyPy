import os
os.system("cls" if os.name == "nt" else "clear")

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay
    
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
    def __str__(self) -> str:
        return f'{self.full_name()} - {self.email}'
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.full_name())

emp_1 = Employee('Ivo', 'Zelic', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(len(emp_1))

# print('test'.__len__())


# print(emp_1 + emp_2)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())




print('\n')

