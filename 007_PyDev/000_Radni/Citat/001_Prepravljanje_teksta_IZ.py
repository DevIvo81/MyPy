'''
Na internetu nađite nekakav tekst (citat, ulomak iz knjige …)
i svaku riječ „prepravite“ tako da:

    - Prvo i zadnje slovo ostavite isto 
    - Omogućite korisniku izbor koliko početnih, a koliko 
    zadnjih slova želi „sačuvati“ i na taj način pojačavati razinu 
    (ne)čitljivosti teksta.
    
    - Probajte napraviti sami primjer kada „sačuvate“ po tri slova 
    (tri na početku i tri na kraju) pa dva slova pa jedno.

    - Sva slova u sredini ispremiješate
    - Ispišete novi tekst i pokušate ga pročitati.
    - Ideja je igranje s načinom kako naš mozak čita riječi pa na 
    ovaj način možete provjeriti je li to istina, odnosno do koje 
    razine možete „ispremiješati“ riječi.
'''
import os
from random import sample as smp


def unosIPretvorbaTekstaUListuRijeci():
    
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        tekstUnos = input('Upišite ili zalijepite tekst od barem 50 znakova\n\n --> ')
        
        if len(tekstUnos) < 50:
            print('\nPrekratak unos, pokušajte sa duljim tekstom (ENTER za nastavak)!')
            input()
            continue
        
        listaTeksta = tekstUnos.split()
        break
    
    return(listaTeksta)


def jednoSlovo(niz):
        
    # Uzimamo slice riječi bez prvog i zadnjeg slova kao listu,
    # izmiješamo ih pomoću naredbe random.sample(niz, duljina niza)
    # i nakon toga ih pretvorimo u riječ
    
    unutarnjiNiz = ''.join(smp(niz[1 : -1], len(niz[1 : -1])))
    
    # ...Nakon miješanja ih ponovno spajamo sa prvim i 
    # zadnjim slovom i vraćamo takvu riječ
    
    return f"{niz[0]}{unutarnjiNiz}{niz[-1]}"


def dvaSlova(niz):
        
    # Uzimamo slice riječi između drugog i predzadnjeg slova kao listu,
    # izmiješamo ih...
    
    unutarnjiNiz = ''.join(smp(niz[2 : -2], len(niz[2 : -2])))
    
    # ...Nakon miješanja ih spajamo sa prva i zadnja dva slova
    # i vraćamo takvu riječ
    
    return f"{niz[0]}{niz[1]}{unutarnjiNiz}{niz[-2]}{niz[-1]}"


def triSlova(niz):
        
    # Uzimamo slice riječi između drugog i predzadnjeg slova kao listu,
    # izmiješamo ih...
    
    unutarnjiNiz = ''.join(smp(niz[3 : -3], len(niz[3 : -3])))
    
    # ...Nakon miješanja ih spajamo sa prva i zadnja dva slova
    # i vraćamo takvu riječ
    
    return f"{niz[0]}{niz[1]}{niz[2]}{unutarnjiNiz}{niz[-3]}{niz[-2]}{niz[-1]}"


def prepravljanjeTeksta():
    
    # Nova lista započinje kao prazna lista    
    novaTekstLista = []
    
    tekstLista = unosIPretvorbaTekstaUListuRijeci()
    
    while True:
        
        izborIspisa = input('''
        Odaberi fiksna slova:
        - Prvo i zadnje slovo --> 1
        - Prva i zadnja dva slova --> 2
        - Prva i zadnja tri slova --> 3
            
        - Vaš izbor --> ''')
        if izborIspisa == '1':
            for rijec in tekstLista:
                if len(rijec) < 4:
                    novaTekstLista.append(rijec)
                else:
                    rijec = jednoSlovo(rijec)
                    novaTekstLista.append(rijec)
            break
        
        elif izborIspisa == '2':
            for rijec in tekstLista:
                if len(rijec) < 6:
                    novaTekstLista.append(rijec)
                else:
                    rijec = dvaSlova(rijec)
                    novaTekstLista.append(rijec)
            break
        
        elif izborIspisa == '3':
            for rijec in tekstLista:
                if len(rijec) < 8:
                    novaTekstLista.append(rijec)
                else:
                    rijec = triSlova(rijec)
                    novaTekstLista.append(rijec)
            break
        
        else:
            print('\nPogrešan unos!')                   
    
    return novaTekstLista


def ispis():
        
    listaZaIspis = prepravljanjeTeksta()
             
    # Po želji:
    '''
    # Uvlačenje prvog retka
    listaZaIspis[0] = '\t' + listaZaIspis[0]
    # Prebacivanje u novi red nakon 8 riječi 
    # ili po želji
    for i in range(1, len(listaZaIspis)):
        if i % 8 == 0:
            listaZaIspis[i] += '\n'
    '''
        
    print()
    print(*listaZaIspis, sep=' ', end='\n')


while True:

    ispis()
    
    if input('\nNovi unos (0 za prekid)? --> ') == '0':
        print('\nDo sljedećeg puta, pozdrav!\n')
        break
