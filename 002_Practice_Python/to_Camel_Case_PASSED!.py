def to_camel_case(text):
    
    if not text:
        print('No text to convert')
        return text
    else:      
        text = text.strip()
        specials = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' + "'"

        for char in text:
            if char in specials:
                text = text.replace(char, ' ')    
       
        textWordsList = text.split()
        
        for word in textWordsList:

            if word[0].upper():
                word = word.capitalize()
            else:
                word = word.lower()
        
        for i in range(1, len(textWordsList)):
            textWordsList[i] = textWordsList[i].capitalize()

        camelCaseText = ''.join(textWordsList)
        return camelCaseText

text = input('\nPaste some text here --> ')

camelCased = to_camel_case(text)

input('\n\nOriginal text\n\n')
print(text)

input('\n\ncamelCased text\n\n')
print(camelCased)