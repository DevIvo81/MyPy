import os
os.system('cls' if os.name == 'nt' else'clear')

''' 1. ZADATAK
1.  U ovom zadatku potrebno je simulirati nasljeđivanje. Kreirajte 
    bazni razred imena Stavka i dva razreda koji nasljeđuju bazni 
    razred, imena Sok i Hrana.
    
    Bazni razred Stavka mora sadržavati konstruktor  i metodu 
    cijenaPdv(). Konstruktor prima dva parametra, naziv i cijenu 
    bez PDV-a. Metoda cijenaPdv() mora vratiti cijenu s PDV-om (25%).
    
    Razred Sok mora naslijediti bazni razred te mora sadržavati 
    konstruktor i metodu ispis(). Konstruktor prima tri parametara, 
    naziv, cijenu i volumen pića. Primijetite da se naziv i cijena 
    nalaze u baznom konstruktoru. Metoda ispis() mora ispisati 
    naziv, cijenu (bez PDV-a) i volumen pića.
    
    Razred Hrana mora naslijediti bazni razred te mora sadržavati 
    konstruktor i metodu ispis(). Konstruktor prima tri parametara, 
    naziv, cijenu i broj kalorija hrane. Primijetite da se naziv i cijena 
    nalaze u baznom konstruktoru. Metoda ispis() mora ispisati 
    naziv, cijenu (bez PDV-a) i broj kalorija.
    
    U glavnom programu kreirajte dva objekta, jedan razreda Sok, 
    drugi razreda Hrana. Nad svakim objektom pozovite njegovu 
    pripadajuću metodu ispis() te pomoću metode cijenaPdv() 
    iz baznog razreda ispišite cijenu pića ili hrane sa PDV-om.
'''



'''
2.  U ovom zadatku potrebno je simulirati nadjačavanje. Nadogradite 
    prethodni zadatak ove vježbe na način da u izvedenim razredima 
    implementirate metodu cijenaPdv() koja će nadjačati tu istu 
    metodu iz baznog razreda. Tako implementirana metoda za piće 
    mora vratiti cijenu s porezom od 15%, dok za hranu mora vratiti 
    cijenu s porezom od 5%.
'''


class Stavka:
    
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena
    
    def cijenaPDV(self):
        return self.cijena * 1.25


class Sok(Stavka):
        
    def __init__(self, naziv, cijena, volumen):
        super().__init__(naziv, cijena)
        self.volumen = volumen
        
    
    def cijenaPDV(self):
        return self.cijena * 1.15
    
    
    def ispis(self):
            print()
            print(f'NAZIV: {self.naziv}')
            print(f'CIJENA BEZ PDV: {self.cijena} HRK')
            print(f'VOLUMEN: {self.volumen} dl')
            

class Hrana(Stavka):

    def __init__(self, naziv, cijena, broj_kcal):
        super().__init__(naziv, cijena)
        self.broj_kcal = broj_kcal
    
    
    def cijenaPDV(self):
        return self.cijena * 1.05
    
    
    def ispis(self):
            print()
            print(f'NAZIV: {self.naziv}')
            print(f'CIJENA BEZ PDV: {self.cijena}')
            print(f'KALORIJE: {self.broj_kcal} kCal')


sok = Sok('Coca Cola', 20, 5)
sok.ispis()
print(f'\nCijena +15% iznosi {sok.cijenaPDV():.2f} HRK\n')

print()

hrana = Hrana('Big Mac', 25, 1500)
hrana.ispis()
print(f'\nCijena +5% iznosi {hrana.cijenaPDV():.2f} HRK\n')

