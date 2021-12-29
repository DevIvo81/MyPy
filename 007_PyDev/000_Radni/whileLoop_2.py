import os
os.system('cls')

recenica = 'Python programer'

# for slovo in recenica:
#     if slovo == 'g':
#         # TODO
#         break
#     print(slovo, end=' ')
# print()

# for slovo in recenica:
#     if slovo == 'g':
#         # TODO
#         continue
#     print(slovo, end=' ')
# print()

# for slovo in recenica:
#     if slovo == 'g':
#         # TODO
#         pass
#     print(slovo, end=' ')

# print('\nGlavni tijek programa')

while True:
    # sve dok je uvjet točan kod se
    # izvršava
    print('Pozdrav iz beskonačne WHILE petlje')
    odgovor = input('\nŽelite li ponoviti izvršavanje petlje? [ Da = 1 / Ne = 0 ] ')
    if odgovor != '1':
        print('\nOvo više nije beskonačna petlja')
        break
    else:
        pass