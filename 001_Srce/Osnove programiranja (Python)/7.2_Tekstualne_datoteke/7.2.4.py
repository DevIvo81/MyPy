'''4.  * Pomoću programa Notepad kreirajte datoteku i u 10 redaka te 
datoteke napišite po jedan proizvoljan broj. Napišite program koji će 
pročitati tu datoteku te sve parne brojeve iz nje upisati u novu 
datoteku. Također, izračunajte sumu svih neparnih brojeva te ih 
zapišite u treću datoteku.'''

import os
os.system('cls')

suma_nep = 0
with open('Deset_redaka.txt') as f:
    with open('NOVA.txt', 'w') as g:
        with open('NEPARNI.txt', 'w') as h:
            for i in f.readlines():
                if int(i) % 2 == 0:
                    g.writelines(i)
                else:
                    h.writelines(i)
                    suma_nep += int(i)
            h.write('\n' + 'Suma neparnih iznosi ' + str(suma_nep))
