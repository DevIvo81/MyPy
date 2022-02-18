import os
os.system('cls' if os.name == 'nt' else 'clear')

##########

class Demo:
    # Varijabla razreda
    broj = 0
    def __init__(self, naziv):
        # Varijabla objekta
        self.naziv = naziv
        Demo.broj += 1
    
    def ispis(self):
        print(f'\nKreirano instanci:\t{Demo.broj}')
        print(f'\nNaziv instance:\t{self.naziv}')
        print('\n\n')

d1 = Demo('PRVA')
d1.ispis()

d2 = Demo('DRUGA')
d2.ispis()

d3 = Demo('TREĆA')
d3.ispis()


'''

##########

class Osoba:
    
    def __init__(self, ime):
        self.ime = ime
    
    @staticmethod
    def punoljetnaOsoba(godina):
        return godina >= 18

o = Osoba('Marko')

print(Osoba.punoljetnaOsoba(17))
print(Osoba.punoljetnaOsoba(18))


##########

class Osoba:
    
    def __init__(self, ime):
        self.ime = ime
    
    def punoljetnaOsoba(godina):
        return godina >= 18


print(Osoba.punoljetnaOsoba(17))
print(Osoba.punoljetnaOsoba(18))

o = Osoba('Marko')
print(o.punoljetnaOsoba(17))

##########

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    
    def ispisPodataka(self):
        print(f'\nPodaci su : {self.ime}, {self.prezime}')
    
    def hodaj(self):
        print(f'\n{self.ime} hoda')

o1 = Osoba('Ivo', 'Ivić')
o2 = Osoba('Ana', 'Anić')

o1.ispisPodataka()
o2.ispisPodataka()

o1.hodaj()
o2.hodaj()    

##########

class Osoba:
    def __init__(self, vrijednost):
        self.ime = vrijednost
        
o1 = Osoba('Marko')
o2 = Osoba('Marija')

print(o1.ime)
print(o2.ime)
    
########

class Osoba():
    def __init__(self):
        print('\nKreiran je objekt!')

o1 = Osoba()
o2 = Osoba()

#######

class Osoba():
    pass

o1 = Osoba()
o2 = Osoba()
o3 = Osoba()

print(o1, o2, o3, sep='\n')


#######

class Osoba():
    def hodaj(self):
        print('\nHODAJ!')
    
    def sjedni(self):
        print('\nSJEDNI!')
    
    def trci(self):
        print('\nTRČI!')

o = Osoba()

o.hodaj()
o.sjedni()
o.trci()
'''