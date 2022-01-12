def to_camel_case(text):

    import string
    
    specials = string.punctuation
    print(specials)
    strippedText = text.strip()

    for char in specials:
        if char in strippedText:
            strippedText = strippedText.replace(char, ' ')

    firstUpperText = strippedText.title()

    camelCaseText = f'{firstUpperText[0].lower()}{firstUpperText[1 : ]}'

    camelCaseText = camelCaseText.replace(' ', '')

    return camelCaseText

import os
os.system('cls' if os.name == 'nt' else 'clear')

inputText = input('''
Type or paste text for conversion to camelCase.
ENTER will convert "      tHe -  !asHEN  ~_ onE   "

Text goes here--> ''')

if not inputText:
    inputText ='      tHe -  !asHEN  ~_ onE   '

print()
print(to_camel_case(inputText))
input('\nTHE END!\n')
