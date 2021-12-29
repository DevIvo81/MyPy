import os
os.system('cls')

a = int(input("\nUnesi prvi dvoznamenkasti broj: "))
b = int(input("\nUnesi drugi dvoznamenkasti broj: "))
c = a
a = b % 10
print("\n", a)
a = c
b = a % 10
print("\n", b)
