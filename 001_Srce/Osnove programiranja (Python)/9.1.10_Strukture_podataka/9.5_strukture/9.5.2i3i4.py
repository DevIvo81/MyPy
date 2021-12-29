'''2.  Napišite program koji se sastoji od liste. Program s tipkovnice čita 
vrijednosti i tako pročitane vrijednosti sprema u listu. Učitavanje 
prekinuti onoga trenutka kada korisnik unese broj 5. '''

import os
os.system('cls')

lista = []
c = 0
while True:
    os.system('cls')

    print('\nDosad uneseno ==', lista)
    print('\nBrojač unosa ==', c)
    e = input('\nUpiši element liste. "5" prekida unos! : ')
       
    
    if e != '5':
        lista.append(e)
        c+=1
    else:
        if c < 4:
            print('\nMinimalni broj unosa je 4! Pokušaj ponovno!\n')
            input()
        elif c < 6:
            for i in range(3):
                lista[i] = '0'
            print('\nERROR! Upisano je "5"' +
                ' prije 6-og unosa! Prva 3 elementa postaju "0"!\n')                   
            for i in range(len(lista)):
                print('[', i, ']', ' = ', lista[i])
            break            
        else:    
            print('\nUpisano je "5", lista upisanih elemenata prije "5":\n')
            for i in range(len(lista)):
                print('[', i, ']', ' = ', lista[i])
            break

'''3. Nadogradite prethodni zadatak tako da ako je korisnik unio manje od 
6 vrijednosti u listu, na primjer korisnik je unio 3 vrijednosti (četvrta 
unesena vrijednost je 5), ostale 3 vrijednosti neka se postave na 
predefiniranu vrijednost, a to je 0.'''

'''4.  Prethodni zadatak nadogradite tako da nakon završetka upisivanja 
petlja ispiše sve elemente liste zajedno s njihovim pripadajućim 
indeksima. Primjer: 
Unesite broj: 1
Unesite broj: 2
Unesite broj: 3
Unesite broj: 4
Unesite broj: 5 
[0] = 1
[1] = 2 
[2] = 3 
[3] = 4 
[4] = 0 
[5] = 0'''