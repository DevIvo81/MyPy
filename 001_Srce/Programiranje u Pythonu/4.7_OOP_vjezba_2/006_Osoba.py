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
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')

# class Osoba:
#     def __init__(self, imeOsobe):
#         self.imeOsobe = imeOsobe

# o = Osoba('Ivo')
# print(o.imeOsobe)
# o.imeOsobe = 'Ana'
# print(o.imeOsobe)

# print()

'''
2.  Prethodni zadatak prepravite na način da varijabla imeOsobe 
bude zaštićena varijabla. Unutar glavnog programa ispišite 
njenu vrijednost, nakon toga ju promijenite u neku drugu 
proizvoljnu vrijednost te ju ponovo ispišite. Postoji li razlika u 
ponašanju Python programa naspram 1. zadatka?
'''
# class Osoba:
#     def __init__(self, imeOsobe):
#         self._imeOsobe = imeOsobe

# o = Osoba('Ivo')
# print(o._imeOsobe)
# o._imeOsobe = 'Ana'
# print(o._imeOsobe)

# print()

'''
3.  Prethodni zadatak prepravite na način da varijabla imeOsobe 
bude privatna varijabla. Unutar glavnog programa ispišite njenu 
vrijednost, nakon toga ju promijenite u neku drugu proizvoljnu 
vrijednost te ju ponovo ispišite. Postoji li razlika u ponašanju 
Python programa naspram 1. tj. 2. zadatka?
'''

# class Osoba:
#     def __init__(self, imeOsobe):
#         self.__imeOsobe = imeOsobe

# o = Osoba('Ivo')
# print(o.__imeOsobe)
# o.__imeOsobe = 'Ana'
# print(o.__imeOsobe)

# print()


'''
4.  Prethodni zadatk prepravite na način da vrijednost privatne 
varijable imeOsobeispišete unutar glavnog programa iako to 
„nije“ moguće (zaobilaznim putem).
'''

class Osoba:
    def __init__(self, imeOsobe):
        self.__imeOsobe = imeOsobe
        
    def getImeOsobe(self):
        return self.__imeOsobe
    
    def setImeOsobe(self, imeOsobe):
        self.__imeOsobe = imeOsobe
        
    

o = Osoba('Ivo')
print(o.getImeOsobe())
o.setImeOsobe('Pero')
print(o.getImeOsobe())

print()

'''
5.  Prethodni zadatak prepravite na način da za privatnu varijablu 
imeOsobenapišete postavljajuću i dobavljajuću metodu bez 
korištenja dekoratora. Unutar glavnog programa kreirajte jedan 
objekt razreda Osoba. Pomoću postavljajuće i dobavljajuće 
metode pristupite varijabli imeOsobete najprije ispišite njenu 
vrijednost, zatim ju promijenite te ju opet ispišite.
'''


'''
6.  Prethodni zadatak prepravite na način da ostvarite identičnu 
funkcionalnost, no ovog puta koristite dekoratore za postavljajuću 
i dobavljajuću metodu.
'''

class Osoba:
    def __init__(self, imeOsobe):
        self.__imeOsobe = imeOsobe
        
    @property
    def imeOsobe(self):
        return self.__imeOsobe
    
    @imeOsobe.setter
    def imeOsobe(self, imeOsobe):
        self.__imeOsobe = imeOsobe
        
    

o = Osoba('Ivo')
print(o.imeOsobe)
o.imeOsobe = 'Pero'
print(o.imeOsobe)

print()