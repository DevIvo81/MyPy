import os
os.system('cls' if os.name == 'nt' else 'clear')

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        
    def full_name(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Ivo', 'Zelic', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.full_name())
print(Employee.full_name(emp_1))

print()

print(emp_1.email)
print(emp_2.email)

print()

print(emp_1.full_name())
print(emp_2.full_name())


print('\n***END OF PROGRAM***\n\n')

