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

print()
while not brojJePogođen:
    while True:
        print()
        unos = input("Upiši pretpostavljeni broj: ")
        print()
    # ako je unos nije broj slijedi upozorenje
        if unos.isnumeric() == False:
            print("Potrebno je unijeti broj!")
            print()
            # vrati se na početak petlje
            continue
    broj = int(unos)
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