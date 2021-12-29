# određivanje korijena diskriminante kvadratne jednadžbe
# ax2+bx+c --- d=b2-4ac

# Druga verzija

import cmath
a = 1
b = 0
c = 1

d = (b*b-(4*a*c))

print()
print("Diskriminanta je: ", d )
print()
kord1 = cmath.sqrt(d)

print("Korijen diskriminante iznosi: ", kord1)


