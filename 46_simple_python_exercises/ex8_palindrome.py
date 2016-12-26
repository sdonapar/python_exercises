#!/usr/bin/env python

#Define a function is_palindrome() that recognizes palindromes
#(i.e. words that look the same written backwards).
#For example, is_palindrome("radar") should return True .

def is_palindrome(inp_text):
    """ This checks if a given word(s) is a palindrome
        is_palindrome(str) -> bool
    """
    print("Input text:",inp_text)

    start_pos = 0
    end_pos = -1
    inp_text = inp_text.lower()
    while(start_pos < len(inp_text)/2):
        if (inp_text[start_pos] == inp_text[end_pos]):
            start_pos += 1
            end_pos += -1
        else:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("radar"))
    print(is_palindrome("palindrome"))
    print(is_palindrome("effe"))
    print(is_palindrome("Sator Arepo Tenet Opera Rotas"))
