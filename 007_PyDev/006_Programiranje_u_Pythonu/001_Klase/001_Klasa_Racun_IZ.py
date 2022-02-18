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
import os
from datetime import datetime as dt

class Racun:
    
    brojac = 1
    
    
    def __init__(self):
        self.brojRacuna = ''
        self.stavkeRacuna = {}
        self.datumIzdavanja = ''
        self.iznosStavki = 0
        self.iznosPDVa = 0
        self.ukupniIznos = 0
        self.izradaRacuna()
        self.izracunUkupno()
        
    
    def izradaRacuna(self):

        os.system('cls' if os.name == 'nt' else 'clear')
                
        # self.datumIzdavanja = input('Upiši datum izdavanja računa\nu formatu 18.01.2022\n--> ')
        self.datumIzdavanja = '18.01.2022.'

        self.brojRacuna = f'R - {Racun.brojac} - 2022/01'            
        print(self.brojRacuna)
        
        while True:
            
            ime = input('\nArtikl --> ').title()
            cijenaArtikla = float(input('\nCijena (decimalna točka) --> '))
            self.stavkeRacuna[ime] = cijenaArtikla
            
            if not input('\nUNOS ZAVRŠEN? (ENTER za kraj unosa) --> '):
                break
            
        Racun.brojac += 1
    
    
    def izracunUkupno(self):
        
        for cijena in self.stavkeRacuna.values():
            self.iznosStavki += cijena
        
        pdvStopa = 0.25
        
        self.iznosPDVa = self.iznosStavki * pdvStopa
        
        self.ukupniIznos = self.iznosStavki + self.iznosPDVa
    
    
    def ispisRacuna(self):
        print(f'\n{"#" * 30}\n')
        print(f'RAČUN: {self.brojRacuna}')
        print(f'DATUM : {self.datumIzdavanja}\n')
        for stavka, cijena in self.stavkeRacuna.items():
            if len(stavka) < 10:
                print(f' {stavka}:\t\t{cijena:.2f}')
            elif 10 <= len(stavka) < 18:
                print(f' {stavka}:{cijena:.2f}')
            else:
                print(f' {stavka}:\t\t\t{cijena:.2f}')
        print(f'\nUKUPNA CIJENA:\t{self.iznosStavki:.2f}')
        print(f'IZNOS PDV-a:\t{self.iznosPDVa:.2f}')
        print(f'UKUPAN IZNOS:\t{self.ukupniIznos:.2f}')
        print(f'\n{"#" * 30}\n')


sviRacuni = []

while True:
    
    racun = Racun()
    sviRacuni.append(racun)    
    if not input('\nNOVI RAČUN?? (ENTER za izlaz) --> '):
            break
        

for racun in sviRacuni:
    racun.ispisRacuna()
