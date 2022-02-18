'''
Kreirajte aplikaciju za izradu računa
Uz svaki račun čuvajte sljedeće podatke:
    Broj računa
    Datum izdavanja
    Lista Stavki:
        Redni broj - Proizvod 1 - cijena
        Redni broj - Proizvod 2 - cijena
        ...
    Iznos PDV-a
    Ukupan iznos
    Funkcije:
        Obračunaj PDV
        Izračunaj ukupan iznos
        Ispiši račun
        Promijeni stavku
        IzbaciStavku
'''      

class Racun:
    import os
    from datetime import datetime as dt

    
    '''Obračun i izdavanje računa'''
    def __init__(self, brojRacuna, datumRacuna, stavkeRacuna, stopaPDV):
        self.brojRacuna = brojRacuna
        self.datumRacuna = datumRacuna
        self.stavkeRacuna = stavkeRacuna
        self.stavkeUkupno = 0
        self.stopaPDV = stopaPDV
        self.iznosPDV = 0
        self.ukupno()
        self.obracun_PDV()
    
    def ukupno(self):
        for cijena in self.stavkeRacuna.values():
            self.stavkeUkupno += float(cijena)
    
    def obracun_PDV(self):
        self.iznosPDV = self.stavkeUkupno * self.stopaPDV
    
            
    def ispisRacuna(self):
        print(f'RAČUN: {self.brojRacuna}')
        print(f'DATUM : {self.datumRacuna}')
        for stavka, cijena in self.stavkeRacuna.items():
            print(f'\t{stavka} - {cijena}')
        print(f'UKUPNO BEZ PDV-a:\t{self.stavkeUkupno}')
        print(f'IZNOS PDV-a:\t{self.iznosPDV}')
        print(f'UKUPAN IZNOS:\t{self.stavkeUkupno + self.iznosPDV}')
        
def unosStavki(brojacUnosa, pdv):
    
    os.system('cls')
    
    stavkeRacuna = {} 
    
    brojRacuna = f'R - {brojacUnosa} - 2022/01'
    
    datumRacuna = input('\nUpiši datum izdavanja u formatu 18.01.2022 --> ')
    
    while True:
        
        ime = input('\nArtikl --> ')
        cijenaArtikla = float(input('\nCijena (decimalna točka) --> '))
        stavkeRacuna[ime] = cijenaArtikla
        
        
        if not input('\nGotovo? (ENTER za kraj unosa)'):
            
            break
    
    return Racun(brojRacuna, stavkeRacuna, datumRacuna, pdv)

listaRacuna = []
PDV = 0.25
brojac = 1

while True:    
    racun = unosStavki(brojac, PDV)
    listaRacuna.append(racun)
    
    brojac += 1
    
    if not input('\nGotovo? (ENTER za kraj unosa)'):
        break

for racun in listaRacuna:
    racun.ispisRacuna()