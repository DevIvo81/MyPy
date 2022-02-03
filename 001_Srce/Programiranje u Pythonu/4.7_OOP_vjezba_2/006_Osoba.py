import os
os.system('cls' if os.name == 'nt' else 'clear')

'''
1.  Napišite razred imena Osoba te pomoću konstruktora tome 
razredu pridružite atribut imeOsobe. Tako kreirani atribut 
imeOsobe neka bude javna varijabla. U glavnom programu 
kreirajte jedan objekt razreda Osoba te iz njega ispišite vrijednost 
zapisanu u javnoj varijabli imeOsobe (bez korištenja 
dobavljajuće metode). Nakon što ste ispisali vrijednost 
spremljenu u varijabli imeOsobe, unutar glavnog programa 
promijenite tu vrijednost u neku drugu proizvoljnu vrijednost te 
ponovo ispišite vrijednost spremljenu u varijabli imeOsobe.

class Osoba:
    
    def __init__(self, ime_osobe):
        self.ime_osobe = ime_osobe
        
o = Osoba('Ivo')
print(o.ime_osobe)
o.ime_osobe = 'Ana'
print(o.ime_osobe)

'''


'''
2.  Prethodni zadatak prepravite na način da varijabla imeOsobe 
bude zaštićena varijabla. Unutar glavnog programa ispišite 
njenu vrijednost, nakon toga ju promijenite u neku drugu 
proizvoljnu vrijednost te ju ponovo ispišite. Postoji li razlika u 
ponašanju Python programa naspram 1. zadatka?

class Osoba:
    
    def __init__(self, ime_osobe):
        self._ime_osobe = ime_osobe
        
o = Osoba('Ivo')
print(o._ime_osobe)
o._ime_osobe = 'Ana'
print(o._ime_osobe)
'''


'''
3.  Prethodni zadatak prepravite na način da varijabla imeOsobe 
bude privatna varijabla. Unutar glavnog programa ispišite njenu 
vrijednost, nakon toga ju promijenite u neku drugu proizvoljnu 
vrijednost te ju ponovo ispišite. Postoji li razlika u ponašanju 
Python programa naspram 1. tj. 2. zadatka?


class Osoba:
    
    def __init__(self, ime_osobe):
        self.__ime_osobe = ime_osobe
        
o = Osoba('Ivo')
print(o.__ime_osobe)
o.__ime_osobe = 'Ana'
print(o.__ime_osobe)

'''


'''
4.  Prethodni zadatk prepravite na način da vrijednost privatne 
varijable imeOsobeispišete unutar glavnog programa iako to 
„nije“ moguće (zaobilaznim putem).


class Osoba:
    
    def __init__(self, ime_osobe):
        self.__ime_osobe = ime_osobe
        
o = Osoba('Ivo')
print(o._Osoba__ime_osobe)
'''

'''
5.  Prethodni zadatak prepravite na način da za privatnu varijablu 
imeOsobenapišete postavljajuću i dobavljajuću metodu bez 
korištenja dekoratora. Unutar glavnog programa kreirajte jedan 
objekt razreda Osoba. Pomoću postavljajuće i dobavljajuće 
metode pristupite varijabli imeOsobete najprije ispišite njenu 
vrijednost, zatim ju promijenite te ju opet ispišite.

class Osoba:
    
    def __init__(self, ime_osobe):
        self.__ime_osobe = ime_osobe
    
    def get_ime(self):
        return self.__ime_osobe
    
    def set_ime(self, ime):
        self.__ime_osobe = ime
        
o = Osoba('Ivo')
print(o.get_ime())
o.set_ime('Ana')
print(o.get_ime())

'''


'''
6.  Prethodni zadatak prepravite na način da ostvarite identičnu 
funkcionalnost, no ovog puta koristite dekoratore za postavljajuću 
i dobavljajuću metodu.
'''

class Osoba:
    
    def __init__(self, ime_osobe):
        self.__ime_osobe = ime_osobe
    
    @property
    def ime(self):
        return self.__ime_osobe
    
    @ime.setter
    def ime(self, ime):
        self.__ime_osobe = ime
        
o = Osoba('Ivo')
print(o.ime)
o.ime = 'Ana'
print(o.ime)
