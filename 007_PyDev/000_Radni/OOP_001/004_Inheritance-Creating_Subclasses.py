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


class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'--> {emp.full_name()}')



dev_1 = Developer('Ivo', 'Zelic', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Ana', 'Zelic', 90000, [dev_1])

print(issubclass(Manager, Developer))




# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)
# print()
# print(dev_2.email)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

print('\n')

