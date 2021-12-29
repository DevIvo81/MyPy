import os, random
os.system('cls')

# 6. PARKING KARTA I KOVANICE

# Napišite program koji simulira sustav za vraćanje ostatka 
# u aparatu za parking,# koristeći funkcije gdje je zgodno. 
# Neka  program od korisnika učita ubačenu količinu # novca 
# x (x je prirodni broj) i neka mu vrati # ostatak od 6 kuna 
# (cijena sata parkiranja) do ubačene količine kuna. Kod 
# vraćanja ostatka na raspolaganju su kovanice od 5 kuna, 
# 2 kune i 1 kune, pri čemu program treba uvijek vratiti 
# što manju količinu kovanica. 
# Svaku vraćenu kovanicu ispišite.

# Primjerice, ako korisnik upiše x = 17, trebate ispisati:
# Vracam kovanicu od 5 kuna
# Vracam kovanicu od 5 kuna
# Vracam kovanicu od 2 kuna
# Vracam kovanicu od 1 kuna

#kolicina = int(input('\nUpišite količinu novca: '))

print('Hello')

while True:
    
    os.system('cls')
    
    naslov = '  CIJENA PARKIRANJA = 6 kn/h  '
    print(f'{ ( len(naslov) + 1 ) * "*" }'
        f'\n{naslov}'
        f'\n{( len(naslov) + 1) * "*" }')

    k = input('Koliko HRK je ubačeno? ')
    print()
        
    if k.isdigit() == False:
        print('\nBrojevima ne slovima! Pokušaj ponovno.')
        input()
    else:
        
        k = int(k)
        sat = 6
        
        while k > 6:
            
            if (k - 5) >= 6:
                print('Vraćam kovanicu od 5 kuna')
                k -= 5
            
            else:
                if (k - 2) >= 6:
                    print('Vraćam kovanicu od 2 kune')
                    k -= 2
                else:
                    print('Vraćam kovanicu od 1 kune')
                    k -= 1
    
    if input('\nJoš jedna karta? [N za prekid] --> ').upper() == 'N':
            print('\nDo sljedećeg puta, pozdrav!\n')
            break
print()

