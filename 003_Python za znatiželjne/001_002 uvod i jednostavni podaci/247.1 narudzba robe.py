# numeracija stupaca teksta
print()
print()
for i in range(0,5):
    print(i, end='')
    for j in range(1,10):
        print(' ', end='')
print()
print()
for i in range(0,5):
    for j in range(0,10):
        print(j, end='')
print()
print()
# ispis tablice narudžbe proizvoda
proizvod = "Kanta za otpatke"
količina = 50
cijena = 37.42

print("{0:20s} {1:4d} {2:6.2f} {3:8.2f}".format(proizvod, količina, cijena, količina*cijena))

print()

proizvod = "Vješalica"
količina = 170
cijena = 8.56

print("{0:20s} {1:4d} {2:6.2f} {3:8.2f}".format(proizvod, količina, cijena, količina*cijena))

print()

proizvod = "Barski stolac"
količina = 12
cijena = 231.60

print("{0:20s} {1:4d} {2:6.2f} {3:8.2f}".format(proizvod, količina, cijena, količina*cijena))