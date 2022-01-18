'''
1.  Napišite jednostavni razred imena Vozilo. 
    Tako kreirani razred neka bude potpuno 
    prazan, bez atributa i metoda. U glavnom 
    programu kreirajte tri objekta razreda 
    Vozilo i pozivom funkcije 
    print()ispišite podatke o tim trima objektima.
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')

# class Vozilo:
#     pass

# v1 = Vozilo()
# v2 = Vozilo()
# v3 = Vozilo()

# print(v1, v2, v3, sep='\n')

'''
2.  Nadogradite razred imena Vozilo iz prethodnog 
    zadatka na način da unutar njega implementirate 
    dvije metode. Metodu Vozi i metodu Koci. Metoda Vozi 
    neka ispisuje na ekran poruku „Vozi!“, a metoda Koci
    neka ispisuje na ekran poruku „Koci!“. Iz glavnog 
    programa pozovite tako napisane metode nad prethodno 
    kreiranim objektima.
'''

# class Vozilo:
    
#     def vozi(self):
#         print('\nVOZI!')
    
#     def koci(self):
#         print('\nKOČI!')

# v = Vozilo()

# v.vozi()
# v.koci()


'''
3.  Nadogradite razred imena Voziloiz prethodnog 
    zadatka tako da mu pridružite tri atributa 
    (pomoću konstruktora): naziv proizvođača, 
    naziv modela, godište modela.

4.  Nastavno na prethodni zadatak implementirajte 
    metodu objekta imena ispis() koja ispisuje 
    vrijednosti postavljenih atributa. Kreirajte 
    dva objekta razreda Vozilo kojima ćete prilikom 
    kreiranja pridružiti proizvoljne vrijednosti 
    te pozivom metode ispis() ispišite pridružene 
    vrijednosti.
'''

class Vozilo:
    
    def __init__(self, proizvodac, model, godiste) -> None:
        self.proizvodac = proizvodac
        self.model = model
        self.godiste = godiste
    
    def ispis(self):
        print(f'\nProizvođač:\t{self.proizvodac}')
        print(f'Model:\t\t{self.model}')
        print(f'Godište:\t{self.godiste}\n\n')
    
    def vozi(self):
        print('\nVOZI!')
    
    def koci(self):
        print('\nKOČI!')

v1 = Vozilo('Toyota', 'RAV4', 2008)
v2 = Vozilo('Peugeot', '206', 2000)

v1.ispis()
v2.ispis()