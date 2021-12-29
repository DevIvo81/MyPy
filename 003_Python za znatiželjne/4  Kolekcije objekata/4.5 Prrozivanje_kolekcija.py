### 4.5. PROZIVANJE KOLEKCIJA KAO ALTERNATIVA UVJETNIM NAREDBAMA

spol = input("\n\nUpiši spol [muški ili ženski]: " )
print()
uBrakuJe = (input("\n\nJesi li u braku? ") == "da")
print()

'''if spol == "ženski":
    if uBrakuJe:
        status = "udana"
    else:
        status = "neudana"
else:
    if uBrakuJe:
        status = "oženjen"
    else:
        status = "neoženjen"

print("\n", status)'''

#  TO SE MOŽE JEDNOSTAVNIJE IZRAZITI KORIŠTENJEM RJEČNIKA S KLJUČEVIMA
#  "ženski" i "muški" I SMJEŠTANJEM PODATAKA O STATUSU U LISTU VRIJEDNOSTI
#   INDEKSI U LISTAMA SU "0" i "1", ODNOSNO "False" I "True". 

status = {"ženski": ["neudana", "udana"], "muški": ["neoženjen", "oženjen"]}
print()
status["muški"][False]
print()
status["ženski"][0]



