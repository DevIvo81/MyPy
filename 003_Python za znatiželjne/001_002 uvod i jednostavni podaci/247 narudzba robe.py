# numeracija stupaca teksta
for i in range(0,5):
    print(i, end='')
    for j in range(1,10):
        print(' ', end='')
print()

for i in range(0,5):
    for j in range(0,10):
        print(j, end='')
print()

# ispis tablice narudžbe proizvoda
proizvod = "Kanta za otpatke"
količina = 50
cijena = 37.42

#print("%20s %4d %6.2f %8.2f" % (proizvod, količina, cijena, količina*cijena))
print("%-20s %4d %6.2f %8.2f" % (proizvod, količina, cijena, količina*cijena))

proizvod = "Vješalica"
količina = 170
cijena = 8.56

#print("%20s %4d %6.2f %8.2f" % (proizvod, količina, cijena, količina*cijena))
print("%-20s %4d %6.2f %8.2f" % (proizvod, količina, cijena, količina*cijena))