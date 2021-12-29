'''9.  ** Napišite program koji s tipkovnice učitava proizvoljni niz znakova. 
Nad učitanim nizom znakova napravite analizu je li taj niz palindrom 
ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak 
zdesna nalijevo. Na primjer, niz: "Ana voli Milovana." je simetričan 
niz.'''
import os
os.system('cls')

niz = input('\nUnesi niz znakova za provjeru palindroma: ')
#print()
#print(niz)
print()
niz = niz.replace(' ', '')
niz = niz.upper()


prov_lista = list(niz)
lista = list(niz)
#print(*lista, sep=' ')
#print()
lista.reverse()
palindrom = lista
print(*palindrom, sep=' ')

if palindrom == prov_lista:

    print('\nZadani niz je palindrom!')
else:
    print('\nNiz nije palindrom')


