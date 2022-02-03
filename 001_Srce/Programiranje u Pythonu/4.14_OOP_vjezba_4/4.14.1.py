from abc import ABC, abstractmethod
import os
os.system('cls' if os.name =='nt' else 'clear')
'''ZADATAK 1
Napišite apstraktni razred imena Zivotinja. Tako kreirani 
    apstraktni razred neka sadrži apstraktne metode imena 
    glasanje() i pokret(). Napišite još dva razreda imena Pas i 
    Puz, ti razredi neka nasljeđuju apstraktni razred Zivotinja. U 
    glavnom programu kreirajte po jedan objekt razreda Pas i Puz te 
    pozovite implementirane metode koje ispisuju kako se određena 
    životinja glasa i kako se kreće.
'''

class Zivotinja(ABC):
    
    @abstractmethod
    def glasanje():
        pass
    
    @abstractmethod
    def pokret():
        pass

class Pas(Zivotinja):
    
    def __init__(self, ime):
        super().__init__()
        self.ime = ime
    
    def glasanje(self):
        print(f'{self.ime} kaže VAU, VAU!')
    
    def pokret(self):
        print(f'{self.ime} TRČI!')
        

class Puz(Zivotinja):
    
    def __init__(self, ime):
        super().__init__()
        self.ime = ime
    
    def glasanje(self):
        print(f'{self.ime} se ne glasa!')
    
    def pokret(self):
        print(f'{self.ime} PUZI!')


pas = Pas('PAS')
pas.glasanje()
pas.pokret()

print()

puz = Puz('PUŽ')
puz.glasanje()
puz.pokret()

print()