

def jeLiInteger(inputString):
    """Osigurava da je unesen
        cijeli broj i vraća
        unos kao int.
    Args:
        inputString ([str]): ['User TODO']
    """
    while True:
        unos = input(inputString)
        try:
            unos = int(unos)
        except:
            print('\nGREŠKA, upiši broj 0 - 3!')
            continue
        return unos

def jeLiFloat(inputString):
    """Osigurava da je unesen
        decimalni broj i vraća
        unos kao float.
    Args:
        inputString ([str]): ['User TODO']
    """
    while True:
        unos = input(inputString)
        try:
            unos = float(unos)
        except:
            print('\nGREŠKA, upiši broj, može i decimalni!')
            continue
        return unos




