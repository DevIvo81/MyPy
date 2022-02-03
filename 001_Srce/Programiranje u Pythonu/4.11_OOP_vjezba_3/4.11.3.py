import os
from math import pi
os.system('cls' if os.name == 'nt' else'clear')

''' ZADATAK 3
3.  U ovom zadatku potrebno je simulirati preopterečenje metode. 
    Kreirajte razred imena GeometrijskiLik, on neka 
    implementira jednu metodu razreda imena opseg()koja može 
    primiti 0 parametara ili pak maksimalno 3 parametara. Ovisno o 
    broju primljenih parametera ova metoda ispisuje pripadajući 
    rezultat.
    
    0 parametara -- Ispišite poruku o greški (Dogodila se greška!) 
    1 parametar -- ispišite opseg kruga (2 * r * PI)
    2 parametra -- ispišite opseg pravokutinika (2*a + 2*b)
    3 parametra -- ispišite opseg raznostraničnog trokuta (a+b+c) 
    
    U glavnom programu pozovite tako implementiranu metodu 
    razreda imena opseg()na sva 4 moguća načina.
'''

class Geometrijski_Lik:
    
    def opseg(a=None, b=None, c=None):
        
        if a is None and b is None and c is None:
            print('\nDogodila se greška!\n')
        
        elif a is not None and b is None and c is None:
            print(f'\nOpseg kruga je {(2 * a * pi):.2f}\n')
        
        elif a is not None and b is not None and c is None:
            print(f'\nOpseg pravokutnika je {(2 * a + 2 * b):.2f}\n')
        
        else:
            print(f'\nOpseg trokuta je {(a + b + c):.2f}\n')


Geometrijski_Lik.opseg(10, 20, 30)



