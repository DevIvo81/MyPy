import random
random.seed()
šesticaBačena = False
for x in range(3): # tri pokušaja bacanja
    if random.randint(1, 6) == 6:
        print()
        print("Bačena je šestica!")
        print()
        šesticaBačena = True
        break
if not šesticaBačena:
    print()
    print("Šestica nije bačena!")
    print()