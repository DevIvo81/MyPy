from abc import ABC, abstractmethod
from math import pi
import os

os.system('cls' if os.name == 'nt' else'clear')

class Geometrijski_Lik(ABC):
    
    @abstractmethod
    def ime():
        pass
    
    @abstractmethod
    def opseg():
        pass

    @abstractmethod
    def povrsina():
        pass


class Kvadrat(Geometrijski_Lik):
    
    def __init__(self, a):
        super().__init__()
        self.a = a
    
    def ime(self):
        return ('KVADRAT')
    
    def opseg(self):
        return 4 * self.a
    
    def povrsina(self):
        return self.a ** 2


class Krug(Geometrijski_Lik):
    
    def __init__(self, r):
        super().__init__()
        self.r = r
    
    def ime(self):
        return ('KRUG')
    
    def opseg(self):
        return 2 * self.r * pi
    
    def povrsina(self):
        return pi * self.r ** 2 

def ispis(lik):
    print(lik.ime())
    print(f'Opseg = {lik.opseg():.2f}')    
    print(f'Površina = {lik.povrsina():.2f}')
    

kvadrat = Kvadrat(5)
krug = Krug(10)

ispis(kvadrat)
print()
ispis(krug)
print()
