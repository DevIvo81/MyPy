import os, random
os.system('cls')

# 3. KONVERZIJA

# 1 km = 0.6214 milje
# °C u °F - (0°C = 32°F) -- F = C * (9/5) + 32
# 1 kg = 2.2046 lbs
# 1 lit = 0.2642 gal
# 1 kW = 1.3596 HP

while True:

    print()
    
    unos = input(f'Upišite što želite konvetirati, '
            f'veliko slovo određuje izbor'
            f'\n\nUdaljenost, Temperatura, Masa, '
            f'Volumen, Snaga\n\n').lower()

    if unos == 'u':
        km = int(input('\nUpiši broj kilometara koje želiš konvertirati u milje --> '))
        milje = round(km * 0.6214)
        print(f'\n{km} kilometara iznosi {milje} milja')

    elif unos == 't':
        cStupnjevi = int(input('\nUpiši broj °C koje želiš konvertirati u °F --> '))
        fStupnjevi = round(cStupnjevi * (9 / 5) + 32)
        print(f'\n{cStupnjevi} °C iznosi {fStupnjevi} °F\n')

    elif unos == 'm':
        kg = int(input('\nUpiši broj kg koje želiš konvertirati u lbs --> '))
        lbs = round(kg * 2.2046)
        print(f'\n{kg} kg iznosi {lbs} lbs\n')

    elif unos == 'v':
        lit = int(input('\nUpiši broj litara koje želiš konvertirati u galone --> '))
        galUS = round(lit * 0.2642)
        print(f'\n{lit} litara iznosi {galUS} galona\n')

    elif unos == 's':
        kW = int(input('\nUpiši broj kW koje želiš konvertirati u HP --> '))
        hp = round(kW * 1.3596)
        print(f'\n{kW} kW iznosi {hp} HP\n')

    else:
        print('\nPogrešan unos, pokušaj ponovno!\n')
    
    if input('\nNova konverzija? [N za prekid] --> ').upper() == 'N':
            print('\n Do sljedećeg puta, pozdrav!\n')
            break