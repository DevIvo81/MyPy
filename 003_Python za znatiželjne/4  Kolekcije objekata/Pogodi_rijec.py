import locale, os, string

locale.setlocale(locale.LC_ALL, "hrv")

os.system('cls')

pojam = list(input("\n\nUnesi pojam koji tražimo: ").upper())
print("\n\n")
#print(*pojam, sep=' ')
#print("\n\n")
dosad = []
for i in range(len(pojam)):
    dosad.append("_")
#print(*dosad, sep=' ')
pogslova = []
broj = 0

def grafika(broj):
    print("")
    print("Dosad je pogođeno: ", end=" ")
    for i in range(0, len(dosad)):
        print(dosad[i], end=" ")
    print("")
    print("Slova isprobana dosad su: ", end=" ")
    for i in range(0, len(pogslova)):
        print(pogslova[i], end=" ")
    print("")
    if broj == -1: # you won graphic
        print("       0      ")
        print("     ~~|~~    ")
        print("      / \     ")
        print("Spašen sam!")
        print("POBJEDA!")
    elif broj == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif broj == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif broj == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif broj == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif broj == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif broj == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:   # you lost graphic
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("Omča se steže oko vrata i")
        print("javlja se potreba za mokrenjem.")
        print("GAME OVER!")

def unos():

    global dosad
    global broj
    global pojam

    while True:
        slovo = input("Unesi slovo: ").upper()
        
        if slovo in pogslova:
            print("Pazi, to je već isprobano!")
        else: 
            pogslova.append(slovo)
            
            if slovo in pojam:
                print("Bravo, to je točno slovo!")
                for i in range(len(pojam)):
                    if pojam[i] == slovo:
                        dosad[i] = slovo
                    else:
                        print("Ups, nema tog slova!")                    
                        broj += 1

        if broj > 5: # game over!
            grafika(broj)
            break
        elif "_" in dosad:  #nastavi igru
            grafika(broj)
        else:   # POBJEDA!
            grafika(-1)
            break

def igra():
    grafika(broj)
    unos()

if __name__ == "__main__":
    igra()
    print("KRAJ!")
        
        






    
    




















