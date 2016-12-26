#/usr/bin/env python

#Write a function translate() that will translate
#a text into "rövarspråket" (Swedish for "robber's language").
#Thatis, double every consonant and place an occurrence of "o" in between.
#For example, translate("this is fun")
#should return the string "tothohisos isos fofunon"

def translate(inp_text):
    """ This function translates a given text into Swedish"""
    vowels = list('aeiou')
    print("Input text:",inp_text)
    in_between_char = 'o'
    translated_text = ''
    for char in inp_text:
        if char.isalpha() and char not in vowels:
            translated_text += char + in_between_char + char
        else:
            translated_text += char
    return translated_text.lower()

if __name__ == '__main__':
    print(translate("this is fun"))
    print(translate("i am going to school"))
    print(translate("THIS IS important"))
