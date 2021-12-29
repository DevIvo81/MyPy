import os, locale, string
locale.setlocale(locale.LC_ALL, "hrv")

os.system('cls')

pojam = input("\n\nUnesi traženi pojam: ").upper()  # unos pojma

os.system('cls')

print("\nTraženi pojam ima ", len(pojam), " slova.\n")
print("_________    ")
print("|       |    ")
print("|            ")
print("|            ")
print("|            ")
print("|_______     ")
print()

listaPojam = list(pojam)   # pretvaranje pojma(string) u listu
#print(*listaPojam)
#print()
dosad = ['_' for i in range(len(pojam))]
print(*dosad)
print()
pokus = []
red = 0

def grafika(red):
    print("\nDosad pogođeno: ", end=' ')
    print(*dosad, sep=' ')
    print("\nIsprobana slova: ", end=' ')
    print(*pokus, sep=' ')
    print()
    if red == -1:
        print("\nPOBJEDA! TKO ZNA, ZNA!\n")
        print("NAKON ", len(pokus), " SLOVA")
        print("_________    ")
        print("|            ")
        print("|     ~\@/~  ")
        print("|       |    ")
        print("|___  ~/ \~  ")
        print()
        print(*dosad, sep=' ')
    elif red == 0:        
        print("_________    ")
        print("|       |    ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|_______     ")        
        print()
    elif red == 1:        
        print("_________    ")
        print("|       |    ")
        print("|       @    ")
        print("|            ")
        print("|            ")
        print("|_______     ")
        print()
    elif red == 2:        
        print("_________    ")
        print("|       |    ")
        print("|       @    ")
        print("|       |    ")
        print("|            ")
        print("|_______     ")
        print()
    elif red == 3:        
        print("_________    ")
        print("|       |    ")
        print("|       @    ")
        print("|      /|    ")
        print("|            ")
        print("|_______     ")
        print()
    elif red == 4:        
        print("_________    ")
        print("|       |    ")
        print("|       @    ")
        print("|      /|\   ")
        print("|            ")
        print("|_______     ")
        print()
    elif red == 5:        
        print("_________    ")
        print("|       |    ")
        print("|       @    ")
        print("|      /|\   ")
        print("|      /     ")
        print("|_______     ")
        print()
    else:
        print("\nOMČA SE STEŽE... NEMA TE VIŠE!!\n")
        print("_________    ")
        print("|       |    ")
        print("|      ~@~   ")
        print("|     ~/|\~  ")
        print("|     ~/~\~  ")
        print("|_______     ")
        print()
        print(*listaPojam, sep=' ')
        
def igra():
    
    global listaPojam, dosad, red
    brpok = 0

    while True:
        
        slovo = input("\nUnesi slovo: ").upper()
                
        if slovo in pokus:
            print("\nOPREZ!! To je već isprobano!\n")
            red += 1
        else:
            pokus.append(slovo)
            if slovo in listaPojam:
                print("\nBravo, to je točno slovo!\n")
                for i in range(len(listaPojam)):
                    if listaPojam[i] == slovo:
                        dosad[i] = slovo                
            else:
                print("\nNema tog slova!\n")        
                red += 1
        brpok += 1
        
        if red > 5:
            grafika(red)
            break
        elif '_' in dosad:
            grafika(red)
        else:
            grafika(-1)
            break

igra()       



