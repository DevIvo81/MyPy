# Pogađanje nasumičnog broja između 1 i 100 u 10 pokušaja sa 
# for petljom i alternativnim stavkom

import random
random.seed # generator slučajnih brojeva
print("\nPogađanje nasumičnog broja između 1 i 100 u 15 pokušaja\n")
brojKojiPogađamo = random.randint(1, 100)
print()
for i in range(1, 16):
    broj = int(input("Unesi broj koji pogađamo: "))
    print()
    if broj == brojKojiPogađamo:
        print("Bravo, pogodio si u ", i, " pokušaja")
        break
    elif broj < brojKojiPogađamo:
        print("\nVeći je od toga!\n")
    elif broj > brojKojiPogađamo:
        print("\nManji je od toga!\n")
else:
    print("Nisi pogodio u 15 pokušaja")