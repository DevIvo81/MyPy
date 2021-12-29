### 4.4.2. SKUPOVI ###

# Skup je asocijativna kolekcija u kojoj su vrijednosti ujedno i ključevi.

## Na skupove nećemo primjenjivati indeksni [] operator nego skupovne 
# operacije poput ispitivanja pripadnosti, unije, presjeka i drugih.

### Izmjenjivi i neizmjenjivi skupovi definirani su razredima 
# "set" i "frozenset" s mogućnošću izmjene kao jedinom razlikom

#### Skupovima se koristimo a uklanjanje višestrukih elemenata iz
# slijednih kolekcija, za brzu provjeru pripadnosti, unije i presjeci.

##### Primjer restorana u kojemu je hrana subvencionirana

# Python prepoznaje da se radi o skupu jer nema ":" u navođenju
jelovnik = {"pizza", "samoborski kotlet", "varivo"}
print(jelovnik)

"samoborski kotlet" in jelovnik
"salata" in jelovnik

# Da li su ova dva jela samo podskup jelovnika restorana?
# Provjerimo metodom "issubset" i operatorom "<=":

{"samoborski kotlet", "salata"}.issubset(jelovnik)
{"samoborski kotlet", "salata"} <= jelovnik

# Drugi način je metoda "issuperset" ili operator ">="

jelovnik.issuperset({"samoborski kotlet", "salata"})
jelovnik >= {"samoborski kotlet", "salata"}

# Metoda "isdisjoint" vraća logičku vrijednost upita "False" sadržaja skupa.

jelovnik.isdisjoint({"bečki odrezak", "varivo", "rižoto", "juha", "pizza", "kajgana"})

# Ako metodu "isdisjoint" pozovemo negacijom povratna vrijednost će biti "True", ako 
# matični skup nema zajedničkih elemenata sa skupom iz argumenta.
  
not jelovnik.isdisjoint({"bečki odrezak", "varivo", "rižoto", "juha", "pizza", "kajgana"})

# STVARANJE SKUPOVA #

# primjena konstruktora "set" na zadani pobrojivi argument

set(range(10))

# Tvorba skupova vrši se navođenjem slijeda elemenata u {}
## Skp svih ugrađenih nizova:

nizovi = {list, tuple, range, bytes, bytearray}
sorted([x.__name__ for x in nizovi])

{i//2 for i in range(10)} # skup će prikazati elemente bez ponavljanja

[i//2 for i in range(10)] # u listi se vrijednosti ponavljaju za svaki korak


### OPERACIJE I METODE NAD SKUPOVIMA

# UNIJA - izražava se metodom "union" odnosno operatorom "|"

voće = {"jagoda", "breskva", "rajčica"}
povrće = {"rajčica", "salata", "zelje"}
voće.union(povrće)
voće | povrće == voće.union(povrće)

# PRESJEK - izražava se metodom "intersection" odnosno operatorom "&"

voće.intersection(povrće)
voće & povrće

# RAZLIKA - izražava se metodom "difference" odnosno operatorom "-"

voće.difference(povrće)
voće - povrće
povrće - voće

# SIMETRIČNA RAZLIKA - metoda "symetric_difference" odnosno operatorom "^".
# Rezultat ove operacije sadrži elemente koji se pojavljuju u jednom od
# početnih skupova, ali ne u oba

ili_voće_ili_povrće = voće.symmetric_difference(povrće)
ili_voće_ili_povrće
voće ^ povrće

voće.difference_update(povrće)
voće

# MIJENJANJE I KOPIRANJE SKUPOVA

jelovnik.add("rižoto")
jelovnik

drugi_jelovnik = jelovnik.copy()
drugi_jelovnik.add("juha")
jelovnik
drugi_jelovnik

jelovnik.remove("samoborski kotlet") # uklanja element sa zadanom vrijednošću, a ako nema vrijednosti
                                    #  javlja pogrešku
jelovnik

jelovnik.pop() # uklanja slučajno odabrani element (ako ukloni prvi na to se ne treba oslanjati)
jelovnik

jelovnik.clear()    # briše sve elemente iz skupa
jelovnik

### OBILAŽENJE SKUPOVA

# Kao i kod ostalih kolekcija i pobrojivih obekata elementi skupova se obilaze
# standardnom iteracijom pomoću petlje "for"

for jelo in drugi_jelovnik:
    print(jelo)