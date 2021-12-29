
print()
broj = int(input("Unesi broj za koji treba izračunati faktorijel: "))
broj1 = broj
faktorijel = 1
print()

'''
# pomoću for petlje
for i in range (broj, 1, -1):
    faktorijel *= i
print("{0}! = {1}".format(broj, faktorijel))
print()
'''
# pomoću while petlje

while broj > 1:
    faktorijel *= broj
    broj -= 1

print("{0}! = {1}".format(broj1, faktorijel))
print()   