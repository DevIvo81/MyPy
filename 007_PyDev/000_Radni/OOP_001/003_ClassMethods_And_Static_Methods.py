import os
os.system("cls" if os.name == "nt" else "clear")

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'
        
        Employee.num_of_emps += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Ivo', 'Zelic', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

import datetime as dt

my_date = dt.date(2022, 2, 7)

print(Employee.is_workday(my_date))


print('\n')
