import random    # potrebno za generiranje slučajnih brojeva
# definiramo raspon vrijednosti
najmanji = 1
najveći = 100
print()
print("Pogodi broj između {0} i {1}".format(najmanji, najveći))
print()
random.seed    # inicijaliziramo generator slučajnih brojeva
# generiramo broj koji treba pogoditi
brojKojiPogađamo = random.randint(najmanji, najveći)
brojJePogođen = False # ime koje upravlja izlaskom iz petlje
brojPokušaja = 0
# pogađanje smještamo u petlju koja se ponavlja sve dok broj nije pogođen
while not brojJePogođen:
    print()
    while True:
        broj = int(input("Upiši pretpostavljeni broj: "))
    # ako je broj iz dozvoljenog raspona iskoči iz petlje
        if broj >=najmanji and broj <=najveći:
            break
        print("Broj mora biti između {0} i {1}".format(najmanji, najveći))
    brojPokušaja += 1
    print()
    if broj > brojKojiPogađamo:
        print()
        print("Manji je od toga!")
        print()

    elif broj < brojKojiPogađamo:
        print()
        print("Veći je od toga!")
        print()
    else:
        print()
        print("Bravo, pogodak u ", brojPokušaja, " pokušaja!")
        brojJePogođen = True # ovim postižemo okončanje petlje
        print()





