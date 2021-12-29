import os, math
from math import pow

os.system('cls')

a = int(input("\nUpiši prvi broj: "))
b = int(input("\nUpiši drugi broj: "))

print("\nKvadrat zbroja (a + b)**2 == ", pow(a,2) + 2*a*b + pow(b,2))
