from abc import ABC, abstractmethod
from math import pi
import os

os.system('cls' if os.name == 'nt' else'clear')

#region BEZ ULANČAVANJA METODA
'''
class Gradovi:
    
    def __init__(self, naziv = None):
        self.naziv = naziv
        
    def ispis(self):
        print(f'\n{self.naziv}\n')

    def zagreb(self):
        self.naziv = 'ZAGREB'
    
    def split(self):
        self.naziv = 'SPLIT'
        

g = Gradovi()

g.zagreb()
g.ispis()
g.split()
g.ispis()

'''
#endregion


#region ULANČANE METODE

class Gradovi:
    
    def __init__(self, naziv = None):
        self.naziv = naziv
        
    def ispis(self):
        print(f'\n{self.naziv}\n')
        return self

    def zagreb(self):
        self.naziv = 'ZAGREB'
        return self
    
    def split(self):
        self.naziv = 'SPLIT'
        return self
        

g = Gradovi()

g.zagreb().ispis().split().ispis()
