print()
spol = input("Upiši spol [m ili ž]: ")
print()
uBrakuuJe = (input("Jesi li u braku? ") == "da")
print()

if spol == "ž":
    if uBrakuuJe:
        status = "udana"

    else:
        status = "neudana"

else:
    if uBrakuuJe:
        status = "oženjen"
    
    else:
        status = "neoženjen"