import math

a = float(input('Upiši duljinu stranice "a": '))
print()
b = float(input('Upiši duljinu stranice "b": '))
print()
c = float(input('Upiši duljinu stranice "c": '))
print()

s = (a + b + c) / 2  # poluopseg
P = math.sqrt(s * (s-a) * (s-b) * (s-c)) # Heronova formula
print("Površina je ", P) # izraz postaje naredba