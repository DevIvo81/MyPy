for redak in range(1, 11):
    ispisRetka = str()
    for stupac in range(1,redak + 1):
        umnožak = redak * stupac
        ispisRetka += str.format(" {0:>3}", umnožak)
    print(ispisRetka)