import os
os.system('cls' if os.name == 'nt' else 'clear')

def ispitni_odsječak():
    pitanje = ['tko', 'tu']
    print('\nstvarni argument prije poziva: ', pitanje)
    promijeni_pitanje(pitanje)
    print('\nstvarni argument nakon poziva: ', pitanje)
    
# def promijeni_pitanje(lista):
#     # izmijenimo listu
#     lista = ['koga']
#     # ispišimo nakon izmjene...
#     print('\nformalni argument: ', lista)

def nadomjesni_ispitni_odsječak():
    # stvarni argument
    pitanje = ['tko', 'tu']
    print('\nstvarni argument prije poziva: ', pitanje)
    # 1. nadomjesni kod prijenosa argumenata funkcijskog poziva:
    #   stvarni argument se pridružuje lokalnom imenu lista
    lista = pitanje
    # 2. nadomjesni kod tijela funkcije
    lista = ['koga']
    print('\nformalni argument: ', lista)
    # 3. nadomjesni kod izlaska iz funkcije:
    #   formalni argumenti se brišu
    del lista
    # po izlasku iz funkcije ispisujemo stvarni argument
    print('\nstvarni argument nakon poziva: ', pitanje)
    
def promijeni_pitanje(lista):
    # izmijenimo listu
    lista.append('koga')
    # ispišimo nakon izmjene...
    print('\nformalni argument: ', lista)

ispitni_odsječak()

print('\n')

# nadomjesni_ispitni_odsječak()

# print('\n')
