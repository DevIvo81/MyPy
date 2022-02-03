'''
1.  Napišite jednostavni razred imena Vozilo. 
    Tako kreirani razred neka bude potpuno 
    prazan, bez atributa i metoda. U glavnom 
    programu kreirajte tri objekta razreda 
    Vozilo i pozivom funkcije 
    print()ispišite podatke o tim trima objektima.
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Vozilo:
    pass

v1 = Vozilo()
v2 = Vozilo()
v3 = Vozilo()

print(v1, v2, v3, sep='\n')

'''



'''
2.  Nadogradite razred imena Vozilo iz prethodnog 
    zadatka na način da unutar njega implementirate 
    dvije metode. Metodu Vozi i metodu Koci. Metoda Vozi 
    neka ispisuje na ekran poruku „Vozi!“, a metoda Koci
    neka ispisuje na ekran poruku „Koci!“. Iz glavnog 
    programa pozovite tako napisane metode nad prethodno 
    kreiranim objektima.

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Vozilo:
    
    def vozi(self):
        print('\nVozi!')
    
    
    def koci(self):
        print('\nKoči!\n')
        

v1 = Vozilo()
v1.vozi()
v1.koci()
'''


'''
3.  Nadogradite razred imena Vozilo iz prethodnog 
    zadatka tako da mu pridružite tri atributa 
    (pomoću konstruktora): naziv proizvođača, 
    naziv modela, godište modela.

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Vozilo:
    
    def __init__(self, proizvodac, model, godiste):
        self.proizvodac = proizvodac
        self.model = model
        self.godiste = godiste
    
    def vozi(self):
        print('\nVozi!')
    
    
    def koci(self):
        print('\nKoči!\n')
        

def novo_vozilo():
    
    print('\nDODAVANJE NOVOG VOZILA\n')
    proizvodac = input('\nProizvođač? --> ').title()
    model = input('\nModel? --> ').upper()
    while True:
        try:
            godiste = int(input('\nGodiste? --> '))
            break
        
        except Exception as e:
            print(f'\nERROR --> {e}')
    
    
    
    
    return Vozilo(proizvodac, model, godiste)


v1 = Vozilo('Toyota', 'RAV4', 2008)
v2 = Vozilo('Peugeot', '206', 2000)

'''

    
'''
4.  Nastavno na prethodni zadatak implementirajte 
    metodu objekta imena ispis() koja ispisuje 
    vrijednosti postavljenih atributa. Kreirajte 
    dva objekta razreda Vozilo kojima ćete prilikom 
    kreiranja pridružiti proizvoljne vrijednosti 
    te pozivom metode ispis() ispišite pridružene 
    vrijednosti.
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

class Vozilo:
    
    def __init__(self, proizvodac, model, godiste):
        self.proizvodac = proizvodac
        self.model = model
        self.godiste = godiste
    
    
    def ispis(self):
        print(f'\nPODACI O VOZILU\n')
        print(f'\nPROIZVOĐAČ -->\t{self.proizvodac}')
        print(f'\nMODEL -->\t{self.model}')
        print(f'\nGODIŠTE -->\t{self.godiste}\n')
    
    
    def vozi(self):
        print('\nVozi!')
    
    
    def koci(self):
        print('\nKoči!\n')
        



def novo_vozilo():
    
    print('\nDODAVANJE NOVOG VOZILA\n')
    proizvodac = input('\nProizvođač? --> ').title()
    model = input('\nModel? --> ').upper()
    while True:
        try:
            godiste = int(input('\nGodiste? --> '))
            break
        
        except Exception as e:
            print(f'\nERROR --> {e}')
    
    
    
    
    return Vozilo(proizvodac, model, godiste)


v1 = Vozilo('Toyota', 'RAV4', 2008)
v2 = Vozilo('Peugeot', '206', 2000)



v1.ispis()
v2.ispis()


