'''5.  Napravite hrvatsko-engleski rječnik. Ključ podataka neka bude 
hrvatska riječ, a vrijednost toga ključa neka bude engleska riječ. 
Napuniti rječnik s 5 elemenata. 
Napraviti beskonačnu petlju koja učitava s tipkovnice hrvatske riječi. 
Za svaku učitanu riječ (ako prijevod postoji) ispisati prijevod, a ako 
tražena riječ ne postoji, ispisati poruku da ta riječ ne postoji u 
rječniku. 
Učitavanje raditi tako dugo dok se ne unese znak 'x'. Potrebno je 
obratiti pažnju na mala/velika slova. Prijedlog je pretvarati sve u mala 
slova.'''

import os
os.system('cls')

hrv_eng = {'jabuka' : 'apple', 'olovka' : 'pencil', 'knjiga' : 'book', 'automobil' : 'car', 'kuhinja' : 'kitchen'}

print(hrv_eng)

dosad = []

while True:
    
    hrv = input('\nUnesi hrvatsku riječ: ')
    
    if hrv.lower() == 'x':
        print('\nGOTOVO!')
        print('\nIsprobane riječi: ', *dosad, sep=' ')
        break
    
    else:    
        if hrv not in hrv_eng.keys():
            print('\nGREŠKA! Te riječi nema u rječniku!')
            dosad.append(hrv)
        else:
            print('\n', hrv_eng[hrv])
            dosad.append(hrv)
            
        
    
            

