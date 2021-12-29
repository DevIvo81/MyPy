# PRIMJER ISTOVREMENOG KORIŠTENJA RJEČNIKA I SKUPA

tekst = """Jedna je mačka živjela sama
u svome stanu kao dama, 
i tamo joj je bilo krasno;"""

# iz ovog teksta stvaramo rječnik u kojem će ključ biti slovo, 
# a vrijednost broj pojavljivanja tog slova u tekstu

import string  # modul za nizove znakova

zaIzbaciti = string.whitespace + string.punctuation # prikupljanje svih izraza razmaka i
                                                    # interpunkcije
zaIzbaciti

# Statička metoda "maketrans" ovdje koristi 3 argumenta, gdje treći argument
# sadrži znakove koje želimo obrisati
tekst = tekst.translate(str.maketrans('', '', zaIzbaciti)).lower()
tekst
H = {slovo: tekst.count(slovo) for slovo in set(tekst)}
H