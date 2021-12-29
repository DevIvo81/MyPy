import os
os.system('cls')

a = "saMo dArK sOuLS i sLIčno"
print("\n",a, "\n")

mala = 0
velika = 0

for i in range(len(a)):
    if a[i] != ' ':
        
        if a[i].isupper() == True:
            velika += 1
        else:
            mala += 1
    if a[i] == "O":
        print('\nSlovo "O" je pronađeno. Zaustavlja se brojanje!')
        break


print("\nU traženom pojmu ima ", velika, " velikih i ", mala, " malih slova\n")

    