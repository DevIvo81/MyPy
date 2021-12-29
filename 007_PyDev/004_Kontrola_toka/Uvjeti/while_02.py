# recenica = 'Python programer'

# for slovo in recenica:
#     if slovo == 'g':
#         break
#     print(slovo, end=' ')

# print()
# print('Glavni tijek programa')


# recenica = 'Python programer'

# for slovo in recenica:
#     if slovo == 'g':
#         continue
#     print(slovo, end=' ')

# print()
# print('Glavni tijek programa')


# recenica = 'Python programer'

# for slovo in recenica:
#     if slovo == 'g':
#         # TODO
#         pass
#     print(slovo, end=' ')

# print()
# print('Glavni tijek programa')


while True:
    print('Pozdrav iz beskonacne WHILE petlje')

    # kod u nasoj WHILE petlji

    odogovor = int(input('Zelite li ponoviti izvrsavanje petlje? (Da=1/Ne=0) '))
    if odogovor != 1:
        print()
        print('Ovo vise nije beskonacna petlja')
        break
    else:
        pass


print()
print('Glavni dio programa')