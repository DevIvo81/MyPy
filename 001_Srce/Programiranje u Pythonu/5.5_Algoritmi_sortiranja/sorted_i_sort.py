import os
os.system('cls' if os.name == 'nt' else'clear')

#region sorted()
'''
lista = [6, 4, 8, 5, 10, 7, 3, 1, 9]
print(f'lista: {lista}\n')

sortirana_lista = sorted(lista)

print('Liste nakon korištenja funkcije sorted():')
print('lista:', lista)
print('Sortirana lista:', sortirana_lista)
'''
#endregion


#region sort()

lista = [6, 4, 8, 5, 10, 7, 3, 1, 9]
print(f'lista: {lista}\n')

lista.sort()

print('Lista nakon korištenja metode sort():')
print('lista:', lista)

#endregion

