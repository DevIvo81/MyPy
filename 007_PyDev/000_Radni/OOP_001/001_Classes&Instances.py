import os
os.system('cls' if os.name == 'nt' else 'clear')

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        
        Employee.num_of_emps += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

emp_1 = Employee('Ivo', 'Zelic', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)


print('\n***END OF PROGRAM***\n\n')

