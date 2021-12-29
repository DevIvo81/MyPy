'''5. Napišite program koji s tipkovnice učitava tri cijela broja: redni broj 
dana u mjesecu, redni broj mjeseca u godini i redni broj godine. 
Prekontrolirajte jesu li učitane vrijednosti ispravne (ispravne 
vrijednosti su: dan - [1, 31], mjesec - [1, 12], godina - [0, 2020]). Za 
ulazne podatke 19, 2, 2017, ispišite datum u sljedećem formatu:
19. veljače, 2017.'''

dan = int(input("Unesi dan: "))
mjesec = int(input("Unesi mjesec: "))
god = int(input("Unesi godinu: "))

if 1<=dan<=31 and 1<=mjesec<=12:
    if mjesec == 1:
        mjesec = "siječnja, "
        print("\n",dan, ". ", mjesec, god, ".")
        
    elif mjesec == 2:
        mjesec = "veljače, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 3:
        mjesec = "ožujka, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 4:
        mjesec = "travnja, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 5:
        mjesec = "svibnja, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 6:
        mjesec = "lipnja, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 7:
        mjesec = "srpnja, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 8:
        mjesec = "kolovoza, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 9:
        mjesec = "rujna, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 2:
        mjesec = "listopada, "
        print("\n",dan, ". ", mjesec, god, ".")

    elif mjesec == 2:
        mjesec = "studenog, "
        print("\n",dan, ". ", mjesec, god, ".")

    else:
        mjesec = "prosinca, "
        print("\n",dan, ". ", mjesec, god, ".")