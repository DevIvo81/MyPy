def to_camel_case(text):
    #your code goes here

    # text = input('\nPaste some text here --> ')

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
            print(strippedText)
            camelCaseText = strippedText.title()
            camelCaseText = camelCaseText.replace(' ', '')
            
        else:
            
            firstUpperText = strippedText.title()
            camelCaseText = f'{firstUpperText[0].lower()}{firstUpperText[1 : ]}'
            camelCaseText = camelCaseText.replace(' ', '')
        
        print(camelCaseText)
        
        return camelCaseText

print(to_camel_case('the-steaLTh-waRrior'))