'''3.  S tipkovnice učitajte broj proizvoljne vrijednosti. Za tako učitan 
broj provjerite zadovoljava li on uvjet: 10 < broj < 30, ako je 
uvjet zadovoljen, ispišite na ekran: "Zadovoljava!", ako pak uvjet 
nije zadovoljen, ispišite na ekran: "Ne zadovoljava!". Ovaj 
zadatak potrebno je riješiti korištenjem operatora usporedbe, bez 
korištenja logičkih operatora i logičkih izraza.'''
import os
os.system('cls')

a = int(input('\nUpiši broj: '))

if 10 < a < 30:
    print('\nZadovoljava!')
else:
    print('\nNe zadovoljava!')
