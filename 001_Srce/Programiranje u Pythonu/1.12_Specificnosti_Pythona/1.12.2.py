'''2.  U dvije varijable inicijalizirajte dva različita proizvoljna broja. 
Nakon inicijalizacije ispišite vrijednosti varijabli na zaslon. 
Zamijenite vrijednosti tih dviju varijabli te ponovo ispišite njihove 
nove vrijednosti. '''
import os
os.system('cls')

a, b = 10, 88
print(a, b)
b, a = a, b
print(a, b)