import os

os.system('cls')

while True:
    a = int(input("\nUnesi prvi broj: "))
    b = int(input("\nUnesi drugi broj manji od prvog: "))
    c = a
    if b > a:
        print("\nDrugi broj mora biti manji od prvog!\n")
    
    else:
        print("\nZbroj upisanih brojeva iznosi ", a + b)
        print("\nRazlika upisanih brojeva iznosi ", a - b)
        print("\nUmnožak upisanih brojeva iznosi ", a * b)
        print("\nKvocijent upisanih brojeva iznosi ", a / b)
        print("\nOstatak dijeljenja upisanih brojeva iznosi ", a % b)
        print("\nCjelobrojno dijeljenje upisanih brojeva iznosi ", a // b)
        print("\nPotenciranje upisanih brojeva iznosi ", a ** b)
        print()
        a += b
        print("\nZbroj upisanih brojeva iznosi ", a)
        a = c
        a -= b
        print("\nRazlika upisanih brojeva iznosi ", a)
        a = c
        a *= b
        print("\nUmnožak upisanih brojeva iznosi ", a)
        a = c
        a /= b
        print("\nKvocijent upisanih brojeva iznosi ", a)
        a = c
        a %= b
        print("\nOstatak dijeljenja upisanih brojeva iznosi ", a)
        a = c
        a //= b
        print("\nCjelobrojno dijeljenje upisanih brojeva iznosi ", a)
        a = c
        a **= b
        print("\nPotenciranje upisanih brojeva iznosi ", a)
        
    if input("\nŽelite li pokušati ponovno? [DA/NE]").upper() == 'NE':
        break

a = int(input("\nUnesi prvi broj: "))
b = int(input("\nUnesi drugi broj manji od prvog: "))



    
