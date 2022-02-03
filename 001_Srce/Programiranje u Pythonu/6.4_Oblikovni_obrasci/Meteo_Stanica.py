from abc import ABC, abstractmethod

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Subjekt
class Meteostanica:
    
    def __init__(self) -> None:
        self.__prijavljeni_uredaji = set()
        self.__temp = None
        self.__vlaga = None
    
    def dodaj_uredaj(self, o):
        self.__prijavljeni_uredaji.add(o)
        o.izvor_informacija = self
        
    def ukloni_uredaj(self, o):
        self.__prijavljeni_uredaji.discard(o)
        o.izvor_informacija = None
        
    def __obavijesti(self):
        print('\nNovi podaci:\n')
        for o in self.__prijavljeni_uredaji:
            o.osvjezi(self.__temp, self.__vlaga)
        
    @property
    def temperatura(self):
        return self.__temp
    
    @temperatura.setter
    def temperatura(self, v):
        self.__temp = v
        self.__obavijesti()
        
    
    @property
    def vlaznost(self):
        return self.__vlaga
    
    @vlaznost.setter
    def vlaznost(self, v):
        self.__vlaga = v
        self.__obavijesti()
        
        

# Promatrač
# Apstraktni razred

class Uredaj(ABC):

    def __init__(self):
        self.izvor_informacija = None
        self.__temp = None
        self.__vlaga = None

    @abstractmethod
    def osvjezi(self, v1, v2):
        pass


# Konkretan promatrač 1
# Naslijeđen apstraktni razred - Uredaj

class Zaslon_Za_Prikaz(Uredaj):
    
    def __init__(self, naziv):
        super().__init__()
        self.__naziv = naziv
        
    def osvjezi(self, t, v):
        self.__temp = t
        self.__vlaga = v
        
        print(f'\tPromatrač: {self.__naziv}')
        print(f'\t\tTemperatura: {self.__temp}')
        print(f'\t\tVlažnost: {self.__vlaga}')
        
        

# Konkretan promatrač 2
# Naslijeđen apstraktni razred - Uredaj

class Mobilna_Aplikacija(Uredaj):
    
    def __init__(self, naziv):
        super().__init__()
        self.__naziv = naziv
        
    def osvjezi(self, t, v):
        self.__temp = t
        self.__vlaga = v
        
        print(f'\tPromatrač: {self.__naziv}')
        print(f'\t\tTemperatura: {self.__temp}')
        print(f'\t\tVlažnost: {self.__vlaga}')

# Glavni program

ms = Meteostanica()

blagovaonica = Zaslon_Za_Prikaz("Blagovaonica")
dnevna = Zaslon_Za_Prikaz("Dnevna soba")
kupaonica = Zaslon_Za_Prikaz("Kupaonica")
spavaca = Zaslon_Za_Prikaz("Spavaća soba")
mobitel = Mobilna_Aplikacija('Mobitel')
tablet = Mobilna_Aplikacija('Tablet')

ms.dodaj_uredaj(blagovaonica)
ms.dodaj_uredaj(dnevna)
ms.dodaj_uredaj(spavaca)
ms.dodaj_uredaj(mobitel)

ms.temperatura = 24
ms.vlaznost = 40

ms.ukloni_uredaj(dnevna)
ms.ukloni_uredaj(spavaca)

ms.temperatura = 23
ms.vlaznost = 41
