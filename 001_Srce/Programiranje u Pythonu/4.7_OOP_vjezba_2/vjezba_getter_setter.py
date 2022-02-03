import os
os.system('cls' if os.name == 'nt' else'clear')

class Osoba:
    
    def __init__(self, ime):
        self._ime = ime
        
    @property
    def ime(self):
        return self._ime
    
    @ime.setter
    def ime(self, vrijednost):
        self._ime = vrijednost

o = Osoba('Ivica')
print(o.ime)
o.ime = "Perica"
print(o.ime)
