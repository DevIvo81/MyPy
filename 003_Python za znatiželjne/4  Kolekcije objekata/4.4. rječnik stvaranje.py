# Rječnici ne pripadaju u slijedne (nizane) kolekcije. Elementi nisu indeksirani...
# ... i poredani već im se pristupa neizmjenjivim ključevima.

# Literale rječnika izražavamo nizom parova, "ključ: vrijednost" u {}.

engHrv = {"alias": "inače zvan", "hash": "sasjeckati"}
print()
engHrv['hash']
print()

# Rječnici su izmjenjivi objekti tako da im elemente možemo po volji dodavati
# ili brisati, ali i mijenjati ako su izmjenjivog tipa.

namirnice = {"čokolada":["smeđe", "ukusno", "zdravo"], 
            "kelj": ["zeleno", "izvrsno", "zdravo"], 
            "luk": ["bijelo", "smrdljivo", "zdravo"], 
            "špek": ["crveno", "njam", "nezdravo"]}
type(namirnice)
print(namirnice)

namirnice[1]
namirnice['luk']

# Nove elemente u rječnik dodajemo tako da ključu koji ne postoji u rječniku
# pridružimo novu vrijednost.

namirnice['rajčica'] = ["crveno", "kiselkasto", "zdravo"]
print(namirnice)

# Istom sintaksom se služimo i za zadavanje nove vrijednosti postojećeg ključa

namirnice['čokolada'] = ["bijelo", "relativno ukusno", "nezdravo"]

# Brisanje elemenata vrši se naredbom "del"

del namirnice['špek']
print(namirnice)

# Osim navođenjem literala unutar {} rječnik se može stvarati i pozivom
# konstruktora "dict" nad pobrojivim (iterabilnim) argumentom

tablica = dict([('rajčica', 'povrće'), ('jabuka', 'voće')])
tablica['rajčica']

tablica = dict(rajčica = 'povrće', (jabuka ='voće')])
print()
tablica['rajčica']
print()
tablica['jabuka']

print("\n\n")

# literale malih rječnika praktično je stvarati putem konstruktora 'dict'
## obratiti pažnju na sintaksu pridruživanja i pozivanja ključeva
cjenik = dict(ćevapi=30, ražnjići=25)
cjenik['ćevapi']

# Iterator "zip" pogodan za uparivanje prikladno konstrukciji rječnika
tablica = dict(zip(['luk', 'jabuka'], ['povrće', 'voće']))
print()
tablica['luk']
print()

# Izrazi za tvorbu rječnika navode se unutar {}, pri čemu se 
# prvi ključ i drugi element odvajaju dvotočkom
## Elementi za tvorbu rječnika mogu biti proizvoljni izrazi

L = "Ivo", "Zelić", 40
{L[0]+' '+ L[1]: L[2]}

# Obuhvaćajući (comprehension) izrazi za tvorbu rječnika
# rječnik koji znakovima koji predstavljaju znamenke pridružuje njihove
# brojčane vrijednosti

znamenke = {chr(48+x): x for x in range(5)}
znamenke['3']

x = dict(enumerate('01234'))
x[0]
znamenke == {k: v for v, k in x.items()}

# članska funkcija "fromkeys" za stvaranje rječnika
# sa istom vrijednosti u svim ključevima
## U prvom argumentu dolazi niz ključeva,
## a u drugom njihova zajednička vrijednost

tablica = dict.fromkeys(('rajčica', 'luk'), "povrće")
tablica['rajčica']
tablica['luk']

# U slučaju izmjenjivih vrijednosti funkciju "fromkeys" izbjegavamo,
# jer bi tada svi elementi rječnika bili vezani za isti objekt.

nabava = dict.fromkeys(('rajčica', 'luk'), [])
nabava['rajčica'] == nabava['luk'] == []
nabava['luk'].append('Siniša')  # Siniša treba luk...
nabava['rajčica'].append('Zoran')   #... a Zoran rajčice
nabava['rajčica']                   # KRIVO !!
# vrijednosti u dva različita ključa su predstavljene istim objektom
# to provjeravamo pozivom funkcije id
id(nabava['rajčica']) == id(nabava['luk'])

# problem ćemo riješiti obuhvatnim izrazom koji svakom ključu pridjeljuje...
# ... posebnu listu.

nabava = {k: [] for k in ('rajčica', 'luk')}
nabava['luk'].append('Siniša')
nabava['rajčica'].append('Zoran')
nabava['rajčica']
nabava['luk']

# Standardno ispitivanje pripadnosti se kod rječnika odnosi na ključeve, a ne na vrijednosti
# kao kod ostalih kolekcija

len(namirnice)
'luk' in namirnice
'špek' in namirnice

# Metoda "items" vraća virtualnu kolekciju parova za sve elemente rječnika

namirnice.items()
dict.items(namirnice)

# ključeve svih zdravih namirnica možemo dobiti obuhvatnom listom

zdraveNamirnice = [x for (x, svojstva) in namirnice.items() if 'zdravo' in svojstva]
zdraveNamirnice

# Metoda "keys" vraća virtualnu kolekciju svih ključeva rječnika. Prethodno
# navedeni izraz "luk" ekvivalentan je izrazu "luk" in namirnice.keys():

hrana = namirnice.keys()
hrana

# Metoda values vraća virtualnu kolekciju svih vrijednosti 

kakvoJe = namirnice.values()
kakvoJe

# Prosječan broj svojstava pomoću ugrađene funkcije "sum"
# koja zbraja sve elemente niza zadanog argumentom.

## Iako argument funkcije "sum" izgleda kao tvorba liste 
## kojoj nedostaju [], radi se o generatorskom izrazu,
## koji elemente ne sprema u memoriju (lista), već ih
## računa na zahtjev.

sum(len(x) for x in namirnice.values()) / len(namirnice)

# Objekti koji vraćaju metode "keys", "values" i "items" se
# nazivaju pogledima na rječnik (dictionary views). To su 
# virtualne kolekcije jer elemente ne spremaju u vlastitu memoriju
# nego ih produciraju na zahtjev matičnog rječnika. Prema tome
# u njima se odražavaju sve izmjene rječnika koje se dogode nakon
# njihova stvaranja

cjenik = {}
ključevi = cjenik.keys()
len(ključevi)

cjenik['ćevapi'] = 30
cjenik['čvarci'] = 35
list(ključevi)

# Metoda "update" spaja dva rječnika tako da sve elemente rječnika zadanog
# argumentom dodjeljuje rječniku nad kojim je metoda pozvana. Ako oba
# rječnika imaju element s istim "ključem" izvorna "vrijednost" se 
# prepisuje novom "vrijednošću"

nove_namirnice = {"jaja": ["narančasta", "ukusna", "zdravo"]}
namirnice.update(nove_namirnice)
namirnice

nove_namirnice2 = {"jaja": ["JAJA!", "JAJA!", "JAJA!"]}
namirnice.update(nove_namirnice2)
namirnice['jaja']

# Isto tako metoda "update" prima sve kombinacije argumenata kao
# konstruktor "dict", uključujući i pobrojivi objekt 
# s parovima "ključ-vrijednost" i imenovane argumente što
# omogućuje elegantno dodavanje višestrukih elemenata u postojeći 
# rječnik.

namirnice.update(tuna = ['ružičasto', 'ukusno', 'zdravo'])
namirnice['tuna']
namirnice

# KOPIRANJE RJEČNIKA
# Kopiranje rječnika metodom "copy"

nove_namirnice = namirnice.copy()

# Usporedba imena pokazuje da se radi o različitim objektima 
# istog sadržaja.

id(nove_namirnice) == id(namirnice)  # različite lokacije objekata u memoriji
nove_namirnice == namirnice  # isti sadržaj objekata

# Brisanje i dodavanje elemenata u kopiji ne utječe na original.

del nove_namirnice['čokolada']
len(namirnice), len(nove_namirnice)
nove_namirnice == namirnice

# OBILAŽENJE RJEČNIKA
# Kao i kod n-torki i lista i po rječnicima možemo iterirati naredbom "for".

## Primjer iteracije po sortiranim ključevima, u skladu sa hrvatskim 
## pravilima usporedbe znakovnih nizova:
import locale
locale.setlocale(locale.LC_ALL, "hrv")

for ime in namirnice:
    print("Ključ: " + ime)
    print("Vrijednost: ", namirnice[ime])