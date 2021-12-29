'''Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno 
djeljivi i s 5 i s 13.'''

import os
os.system('cls')

print('\nParni brojevi djeljivi s 5 i 13, između 1 i 1000 su:\n')
for i in range(1, 1001):
    if i % 2 == 0 and i % 13 == 0 and i % 5 == 0:
        print(i, end=' ')
print()
        
         

