import os
os.system('cls')

rjecnik = {1 : "Siječanj", 2 : "Veljača", 3 :
"Ožujak", 4 : "Travanj", 5 : "Svibanj", 6 :
"Lipanj", 7: "Srpanj", 8 : "Kolovoz",9 : "Rujan", 10 
: "Listopad",11 : "Studeni", 12 : "Prosinac"}

print( rjecnik )

rjecnik = {1 : "Siječanj", 2 : "Veljača", 3 : "Ožujak", 
            4 : "Travanj", 5 : "Svibanj", 6 : "Lipanj"}

print(rjecnik[2])
print(rjecnik[6])
print(rjecnik.keys())
rjecnik.update({7 : 'Srpanj'})
print(rjecnik)
print(rjecnik.keys())
print(rjecnik.values())
del rjecnik[7]
del rjecnik[1]
del rjecnik[2]
print(rjecnik)
rjecnik.update({1 : 'Siječanj', 2 : 'Veljača'})
print(len(rjecnik))
