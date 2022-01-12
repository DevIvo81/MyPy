def to_camel_case(text):
    #your code goes here
    if not text:
        print('No text to convert')
        return text
    else:
        
        specials = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"

        strippedText = text.strip()

        for char in specials:
            if char in strippedText:
                strippedText = strippedText.replace(char, ' ')
                

        if strippedText[0].upper():
            print(f'\nSTRIPPED TEXT [0] = {strippedText[0]}\n')
            firstUpperText = strippedText.title()
            camelCaseText = f'{firstUpperText[0].lower()}{firstUpperText[1 : ]}'
            camelCaseText = camelCaseText.replace(' ', '')
        else:
            camelCaseText = strippedText.title()
            camelCaseText = camelCaseText.capitalize()

            camelCaseText = camelCaseText.replace(' ', '')
        
        print(f'\ncCase TEXT [0] = {camelCaseText[0]}\n')
        
        return camelCaseText

print(to_camel_case('THE-sTEALtH_WARRIOR'))