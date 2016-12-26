#!/usr/bin/env python

#Write a function that takes a character
#(i.e. a string of length 1) and returns True
#if it is a vowel, False otherwise

def is_vowel(char):
    """ this functions checks if a given character is a vowel"""
    vowels = list('aeiou')
    # in case if the user provides more than one character as input
    my_char = char[0].lower()
    print("input character provided :", my_char)
    if my_char in vowels:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_vowel('S'))
    print(is_vowel('A'))
    print(is_vowel('e'))
    print(is_vowel('r'))
