import os
os.system('cls')

a=5
b=10 
c=15
d=21

print("\na =", a, "b =", b, "c =", c, "d =", d, sep='  ')
print()

ArSr = (a+b+c+d)/4
print("Aritmetička sredina zadanih brojeva je ", ArSr)

ArSrCijM = int(ArSr)
ArSrCijV = round(ArSr)

print("\nRezultat cjelobrojne aritmetičke sredine zaokružene na manje je ", ArSrCijM)
print("\nKvadrat cjelobrojne aritmetičke sredine zaokružene na manje je ", ArSrCijM**2)

print("\nRezultat cjelobrojne aritmetičke sredine zaokružene na više je ", ArSrCijV)
print("\nKvadrat cjelobrojne aritmetičke sredine zaokružene na više je ", ArSrCijV**2)

kvadrat = ArSrCijM ** 2
kvadrat *= 100
print("\nkvadrat < 500? ", kvadrat < 500)









