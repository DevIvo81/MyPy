'''
5.  Napišite objektno orijentirani program. 
    Razred programa neka bude Studenti 
    neka ima sljedeće metode:

    o metoda koja omogućava dodavanje nove ocjene u listu 
      ocjena (metoda objekta),
    o metoda koja vraća aritmetičku sredinu svih ocjena 
      (metoda objekta),
    o metoda koja vraća, ovisno o zaprimljenom argumentu, 
      broj takvih ocjena u listi ocjena (na primjer, ako je 
      primljena vrijednost 5, metoda mora vratiti broj 
      sakupljenih 5-tica), (metoda objekta),
    o metoda koja vraća ukupan broj dodijeljenih ocjena svim 
      studentima zajedno (statička varijabla i statička metoda), 

    ovaj zadatak napravite na dva načina, s dekoratorom 
    @staticmethod i bez njega.
    
    U glavnom programu kreirajte dva objekta razreda Student, 
    pomoću metode za upis ocjena unesite minimalno 8 proizvoljnih 
    ocjena te ispitajte ispravnost metode koja vraća aritmetičku 
    sredinu ocjena, metode koja vraća koliko ocjena određene 
    vrijednosti je student sakupio i zatim isprobajte metodu koja 
    vraća koliko je ukupno ocjena dodijeljeno svim studentima 
    zajedno.
'''
from itertools import count
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Student:
    
    def __init__(self):
        self.ocjene = []
    
    def upis_ocjena(self):
        broj_ocjena = int(input('\nKoliko ocjena unosimo? --> '))
        for i in range(broj_ocjena):
            ocjena = int(input('\nUpiši ocjenu --> '))
            self.ocjene.append(ocjena)
        
    def ispis_ocjena(self):
        print('\nOCJENE\n')
        print(*self.ocjene)
    
    def broj_ocjene(self):
        ta_ocjena = int(input('\nBroj koje ocjene tražimo? --> '))
        broj = self.ocjene.count(ta_ocjena)
        print(f'Ukupno ima {broj} takve ocjene.')
        
    def ar_sred(self):
        return (sum(self.ocjene) / len(self.ocjene))
    
stu_1 = Student()

input('\nSTUDENT - 1\n')
stu_1.upis_ocjena()
ocjene_1 = stu_1.ocjene
print(f'\nAritmetička sredina iznosi --> {stu_1.ar_sred():.2f}')
stu_1.broj_ocjene()


stu_2 = Student()
input('\nSTUDENT - 2\n')
stu_2.upis_ocjena()
ocjene_2 = stu_2.ocjene
print(f'Aritmetička sredina iznosi --> {stu_2.ar_sred():.2f}')
stu_1.broj_ocjene()

