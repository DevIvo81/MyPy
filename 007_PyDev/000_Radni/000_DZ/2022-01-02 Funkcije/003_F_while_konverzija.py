import os, random
os.system('cls')

# 3. KONVERZIJA

# 1 km = 0.6214 milje
# °C u °F - (0°C = 32°F) -- F = C * (9/5) + 32
# 1 kg = 2.2046 lbs
# 1 lit = 0.2642 gal
# 1 kW = 1.3596 HP

def udaljenost():
    km = int(input('\nUpiši broj kilometara koje želiš konvertirati u milje --> '))
    milje = round(km * 0.6214)
    
    return print(f'\n{km} kilometara iznosi {milje} milja') 

def temperatura():         
    cStupnjevi = float(input('\nUpiši broj °C koje želiš konvertirati u °F --> '))
    fStupnjevi = round(cStupnjevi * (9 / 5) + 32, 1)
    kelvini = round(cStupnjevi + 273.15, 1)
    
    return print(f'\n{cStupnjevi} °C iznosi {fStupnjevi} °F odnosno {kelvini} K\n')

def masa():
    kg = int(input('\nUpiši broj kg koje želiš konvertirati u lbs --> '))
    lbs = round(kg * 2.2046, 2)
    
    return print(f'\n{kg} kg iznosi {lbs} lbs\n')

def volumen():
    lit = float(input('\nUpiši broj litara koje želiš konvertirati u US galone --> '))
    galUS = round(lit * 0.2642, 2)
    
    return print(f'\n{lit} litara iznosi {galUS} galona\n')

def snaga():
    kW = float(input('\nUpiši broj kW koje želiš konvertirati u HP --> '))
    hp = round(kW * 1.3596)
    return print(f'\n{kW} kW iznosi {hp} HP\n')


while True:

    print()
    
    unos = input(f'Upišite što želite konvetirati, '
            f'veliko slovo određuje izbor'
            f'\n\nUdaljenost, Temperatura, Masa, '
            f'Volumen, Snaga\n\n').lower()

    if unos == 'u':
        udaljenost()

    elif unos == 't':
        temperatura()

    elif unos == 'm':
        masa()
        
    elif unos == 'v':
        volumen()
    
    elif unos == 's':
        snaga()

    else:
        print('\nPogrešan unos, pokušaj ponovno!\n')
        continue
    
    if input('\nNova konverzija? [N za prekid] --> ').upper() == 'N':
            print('\nDo sljedećeg puta, pozdrav!\n')
            break

