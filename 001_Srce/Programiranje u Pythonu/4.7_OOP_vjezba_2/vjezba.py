import os
os.system('cls' if os.name == 'nt' else'clear')

class Osoba:
    
    def __init__(self, ime):
        self._ime = ime

o = Osoba('Ivica')

print(o._ime)