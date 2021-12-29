'''** Napišite program koji ispisuje sumu znamenaka nekog 
višeznamenkastog broja. Na primjer, suma broja 159 iznosi 15.
Napomena: 159 % 10 = 9, 159 // 10 = 15'''

import os
os.system('cls')

x = int(input("\nUnesi broj čiji zbroj znamenaka želiš izračunati: "))

a = 0
c = x
suma = 0

print()

while x > 0:
    a = x % 10
    suma += a
    x //= 10
    print(a, end=' + ') 
print("\nSuma znamenaka broja ", c, " iznosi ", suma)




