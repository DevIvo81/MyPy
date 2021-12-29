import random
random.seed()
for x in range(3):
    if random.randint(1, 6) == 6:
        print("\nBačena je šestica!\n")
        break
else:
    print("\nŠestica nije bačena!\n")