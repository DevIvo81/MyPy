import string, locale, os, random

os.system('cls')

locale.setlocale(locale.LC_ALL, "hrv")
print("\n", locale.getlocale(), "\n")

može = list(string.ascii_lowercase + string.ascii_uppercase)
print("\n",može, "\n")

može.append('Ž')
može.insert(45, 'Š')
može.insert(30, 'Đ')
može.insert(30, 'Dž')
može.insert(29, 'Ć')
može.insert(29, 'Č')

može.insert(19, 'š')
može.insert(4, 'đ')
može.insert(4, 'dž')
može.insert(3, 'ć')
može.insert(3, 'č')

for i, j in enumerate(može):
    print(i,": ", j,' ', end=' ')
print('\n'*2)
print("\n",može, "\n")

slova = ['a', 'b', 'c', 'č', 'ć', 'd', 'dž', 'đ', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'š', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'Č', 'Ć', 'D', 'Dž', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'Š', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ž']