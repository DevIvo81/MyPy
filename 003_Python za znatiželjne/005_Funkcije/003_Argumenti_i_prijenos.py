import os, builtins
os.system('cls' if os.name == 'nt' else 'clear')

builtins.print('Proba')

print(id(builtins.print) == id(print))

int = 42

print(int)
print(builtins.int)

builtins.ime = 'ime iz ugrađenog prostora'

print(ime)

ime = 'ime iz globalnog prostora'
print(ime)

del ime

print(ime)