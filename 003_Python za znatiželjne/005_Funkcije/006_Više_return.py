import os, math
os.system('cls' if os.name == 'nt' else 'clear')

def dijeljenje_i_ostatak(x, y):
    
    kvocijent, ostatak = divmod(x, y)

    return f'\nKvocijent brojeva {x} i {y} iznosi {kvocijent} s ostatkom {ostatak}'

print(dijeljenje_i_ostatak(16, 5))
    
    



