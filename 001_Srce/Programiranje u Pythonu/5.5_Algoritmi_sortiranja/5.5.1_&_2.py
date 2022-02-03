import os
os.system('cls' if os.name == 'nt' else'clear')

'''ZADATAK
Pogledajte prethodne dvije liste utrke na 100 metara, sudionici i 
rezultati. Vaš zadatak je da ih sortirate i ispišete uzlazno prema 
rezultatima (od najbržeg do najsporijeg).
1.  Sortiranje napravite pomoću algoritma "sortiranje biranjem" (engl. 
Selection sort).
2.  Sortiranje napravite pomoću poboljšanog algoritma zamjene 
susjednih elemenata (engl. Bubble sort)
'''



def ispis(sudionici, rezultati):
    for i in range(len(rezultati)):
        print(f'{sudionici[i]} --> {rezultati[i]}')


#region SELECTION SORT


'''
sud = ["Ivica", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rez = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]
l = len(rez)

print('Prije sortiranja:')
ispis(sud, rez)

for i in range(l):
    
    min_ind = i
    
    for j in range(i + 1, l):
        if rez[j] < rez[min_ind]:
            min_ind = j
    
    rez[i], rez[min_ind] = rez[min_ind], rez[i]
    sud[i], sud[min_ind] = sud[min_ind], sud[i]

print('\n\nNakon sortiranja:')
ispis(sud, rez)

'''
#endregion





#region BETTER BUBBLE SORT

sud = ["Ivica", "Marica", "Perica", "Nika", "Nikica", "Tihana", "Stjepan", "Petra"]
rez = [10.11, 11.58, 10.08, 10.06, 10.77, 11.22, 11.55, 10.05]
l = len(rez)

print('Prije sortiranja:')
ispis(sud, rez)

for i in range(l):
    swap = False
    for j in range(l - 1):
        if rez[j + 1] < rez[j]:
            rez[j], rez[j + 1] = rez[j + 1], rez[j]
            sud[j], sud[j + 1] = sud[j + 1], sud[j]
            swap = True
    
    if not swap:
        break

print()
print('\n\nNakon sortiranja:')
ispis(sud, rez)

#endregion
