### 4.6. IZMJENA KOLEKCIJA U PETLJAMA

# Razlikujemo dvije vrste postupaka mijenjanja kolekcija.

# 1. Izmjena isključvo elemenata kolekcija, bilo pozivanjem
# izmjenjujućih metoda, bilo dodjelom novih vrijednosti. 

# 2. Postupci koji mijenjaju strukturu kolekcije brisanjem
# postojećih ili umetanjem novih elemenata.

## 4.6.1. IZMJENA ELEMENATA KOLEKCIJA

# IZMJENA ELEMENATA LISTA
# Istodobno iteriranje po indeksima i elementima primjenom
# brojača "enumerate".

osobe = ['marko', 'ana', 'Ivica']   # Neka imena počinju malim slovom!
for i, ime in enumerate(osobe):     # iteracija po indeksima i elementima
    osobe[i] = ime[0].upper() + ime[1:] # za svaki element liste prvo slovo...
                                        #...postaje veliko i dodaje mu se ostatak riječi
osobe

# IZRAZ ZA TVORBU NOVE LISTE

osobe = [ime[0].upper() + ime[1:] for ime in osobe]
osobe

# ZA VIDLJIVOST IZMJENA I PREKO DRUGIH IMENA TE LISTE

osobe = ['marko', 'ana', 'Ivica']
osobe2 = osobe
osobe[:] = [ime[0].upper() + ime[1:] for ime in osobe]
osobe2

# IZMJENA ELEMENATA RJEČNIKA ISTODOBNOM ITERACIJOM PO
# KLJUČEVIMA I VRIJEDNOSTIMA POMOĆU RJEČNIČKOG POGLEDA
# "dict.items()".

cjenik = {'ćevapi': 30, 'ražnjići': 35}
# happy hour: sniženje od 20% na sav roštilj
for k,v in cjenik.items():
    cjenik[k] = round(v*0.8)
print(cjenik)

# IZRAZ ZA TVORBU NOVOG RJEČNIKA
# dodatni popust 10% za studente i učenike!

cjenikStudenti = {k: round(0.9*v) for k,v in cjenik.items()}
print(cjenikStudenti)

# METODA "update()" ZA RJEČNIK S IZMIJENJENIM ELEMENTIMA

# novo sniženje 5% za sve

noviCjenik = {k: round(0.95*v) for k,v in cjenik.items()}
cjenik.update(noviCjenik)
print(cjenik)


### 4.6.2. DODAVANJE I BRISANJE ELEMENATA KOLEKCIJE
# Svi oblici mijenjanja elemenata kolekcije su operacije visokog rizika,
# koje je potrebno izbjegavati. U nastavku slijede sigurni načini 
# iterativnog brisanja elemenata rječnika i lista.

import  locale
locale.setlocale(locale.LC_ALL, "hrv")

# pokušaj brisanja osoba od A do M (OVO NE RADI!)
osobe = ["Marko", "Ana", "Ivica", "Zdravko"]
for i, ime in enumerate(osobe):
    if locale.strcoll(ime[0], 'N') <= 0:
        print("Brišem osobu ", ime, ' na indeksu ', i)
        del osobe[i]
print(osobe)

# pokušaj brisanja osoba od A do M (OVO NE RADI!)
osobe = {"Marko": 78, "Ana": 89, "Ivica": 56, "Zdravko": 65}
for ime in osobe:
    if locale.strcoll(ime[0], 'N') <= 0:
        print("Brišem osobu ", ime)
        del osobe[ime]
print(osobe)
# Nakon prvog prolaza for petlje rječnik je odbio daljnje 
# izvršavanje petlje. 

## BRISANJE ELEMENATA LISTA

# while

osobe = ["Marko", "Ana", "Ivica", "Zdravko"]
## OK ako brišemo mali broj elemenata
i = 0
while i < len(osobe):
    if locale.strcoll(osobe[i][0], 'N') <= 0:
        del osobe[i]
    else:
        i += 1
print(osobe)

# for

osobe = ["Marko", "Ana", "Ivica", "Zdravko"]
## OK ako brišemo mali broj elemenata
for i in range(len(osobe)-1, -1, -1):
    if locale.strcoll(osobe[i][0], 'N') <= 0:
        del osobe[i]

print(osobe)

## brisanje elemenata stvaranjem nove liste
## OK ako je broj brisanja usporediv s duljinom liste
osobe = ["Marko", "Ana", "Ivica", "Zdravko"]
usmeniDanas = [x for x in osobe if locale.strcoll(x[0], 'N') >= 0]
usmeniDanas # Zdravko je prebačen u novu listu

## brisanje elemenata upisom u originalnu listu
## OK ako je broj brisanja usporediv s duljinom liste
osobe[:] = [x for x in osobe if locale.strcoll(x[0], 'N') >= 0]
osobe   # u postojećoj listi je ostao samo Zdravko

### BRISANJE ELEMENATA RJEČNIKA

# iteracija po zasebnoj listi ključeva petljom for

osobe = {"Marko": 78, "Ana": 89, "Ivica": 56, "Zdravko": 65}
for ime in list(osobe.keys()):
    if locale.strcoll(ime[0], 'N') < 0:
        print("Brišem osobu ", ime)
        del osobe[ime]
print(osobe)

# isto postižemo ako u listu za iteraciju dodamo samo 
# ključeve za brisanje

osobe = {"Marko": 78, "Ana": 89, "Ivica": 56, "Zdravko": 65}
zaBrisanje = [ime for ime in osobe 
              if locale.strcoll(ime[0], 'N') >= 0]
for ime in zaBrisanje:
    del osobe[ime]
zaBrisanje
osobe

# I na kraju stvaranjem novog rječnika samo treba paziti da se
# originalnim rječnikom ne koristimo pod drugim imenima ili
# ako nam odgovara da druga imena ne vide izmjene.

osobe = {"Marko": 78, "Ana": 89, "Ivica": 56, "Zdravko": 65}
usmeniDanas = {k: v for k,v in osobe    # stvaranje novog rječnika
              if locale.strcoll(ime[0], 'N') >= 0}  
usmeniDanas
osobe

def faktorijel(x):
    rezultat = 1
    for i in range(1, x+1):
        rezultat *= i
        print(i, end=' * ')
    return rezultat
print(" = ", faktorijel(5), '')