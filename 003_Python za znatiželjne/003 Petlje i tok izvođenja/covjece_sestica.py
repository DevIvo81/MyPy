import os
from random import randint as rnt

os.system('cls' if os.name =='nt' else 'clear')

#region ŠESTICA

for bacanje in range(3):
    if rnt(1, 6) == 6:
        print('\nŠESTICA je bačena!')
        break
    else:
        print('\nŠESTICA NIJE bačena!')

print('\n')

#endregion