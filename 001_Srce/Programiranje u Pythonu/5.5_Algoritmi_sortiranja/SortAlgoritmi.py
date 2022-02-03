#region SELECTION SORT
'''
niz = [7, 4, 2, 8, 6, 1, 3, 5]

print(f'\nNesortirani niz: {niz}')
broj_elemenata = len(niz)

for i in range(broj_elemenata):
    
    min_index = i
    
    for j in range(i + 1, broj_elemenata):
        if niz[j] < niz[min_index]:
            min_index = j
    
    niz[i], niz[min_index] = niz[min_index], niz[i]
    
    print(f'Iteracija: {i + 1} {niz}')

print(f'\nSortirani niz: {niz}')
'''    
#endregion


#region BUBBLE SORT & BETTER BUBBLE SORT

niz = [7, 4, 2, 8, 6, 1, 3, 5]

print(f'\nNesortirani niz: {niz}')
broj_elemenata = len(niz)

for i in range(broj_elemenata - 1):
    zamjena = False
    for j in range(broj_elemenata - 1 - i):
        
        if niz[j + 1] < niz[j]:
            niz[j], niz[j + 1] = niz[j + 1], niz[j]
            zamjena = True
    
    print(f'Prolaz: {i + 1} {niz}')
    
    if zamjena == False:
        break

print(f'\nSortirani niz: {niz}')

#endregion

