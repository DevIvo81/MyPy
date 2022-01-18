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
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Student:
 
    brojacOcjena = 0
    
    def __init__(self, ime, prezime, ocjene=[]):
        self.ime = ime
        self.prezime = prezime
        self.ocjene = ocjene
    
    def novaOcjena(self, ocjena):
        self.ocjene.append(ocjena)
        Student.brojacOcjena += 1

    def arSr(self):
        suma = 0
        broj = 0
        for element in self.ocjene:
            suma += element
            broj += 1
        return round(suma / broj, 2)
    
    def brojOcjena(self, ocjena):
        return self.ocjene.count(ocjena)
    
    def brojSvihOcjena1():
        return Student.brojacOcjena
    
    @staticmethod
    def brojSvihOcjena2():
        return Student.brojacOcjena
    
s1 = Student('Ivo', 'Ivic')
s2 = Student('Ana', 'Anic')

for i in range(int(input(f'\n{s1.ime} {s1.prezime} koliko novih ocjena? --> '))):
    s1.novaOcjena(int(input('\nUpiši ocjenu --> ')))
    
input(f'\nUkupno upisano {Student.brojSvihOcjena1()} ocjena')
input(f'\nProsjek ocjena iznosi {s1.arSr()}')

for j in range(int(input(f'\n{s2.ime} {s2.prezime} koliko novih ocjena? --> '))):
    s2.novaOcjena(int(input('\nUpiši ocjenu --> ')))

input(f'\nUkupno upisano {s2.brojSvihOcjena2()} ocjena')
input(f'\nProsjek ocjena iznosi {s2.arSr()}')