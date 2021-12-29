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
# tražimo od korisnika da upiše svoj pokušaj
broj = int(input("Upiši cijeli broj: "))
print()
# složena naredba if
if broj < brojKojiPogađamo:
    # početak tijela naredbe if
    print("Veći je od tog broja")
elif broj > brojKojiPogađamo:
    # početak tijela naredbe if
    print("Manji je od tog broja")
# nastavak uvjetovanja naredbom else
else:
    print("Bravo, pogodak!")
# naredba nije uvučena pa više ne pripada bloku naredbe if
# i izvodi se neovisno o ishodu gornjeg uvjeta iz naredbe if
print()
print("Pokreni program ponovno za sljedeći pokušaj!")