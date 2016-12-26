#!/usr/bin/env python

"""Write a version of a palindrome recognizer that also accepts
phrase palindromes such as "Go hang a salami I'ma lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil","Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored."""

from ex7_palindrome import is_palindrome

def cleanup(inp_str):
    import re
    pattern = '[^a-z]'
    return re.sub(pattern,'',inp_str.lower())

def new_palindrome(inp_str):
    mod_inp_str = cleanup(inp_str)
    #print("Cleaned input string:",mod_inp_str)
    return is_palindrome(mod_inp_str)

if __name__ == '__main__':
    print(new_palindrome("Go hang a salami I'ma lasagna hog."))
    print(new_palindrome("Was it a rat I saw?"))
    print(new_palindrome("Step on no pets"))
    print(new_palindrome("Sit on a potato pan, Otis"))
    print(new_palindrome("Lisa Bonet ate no basil"))
    print(new_palindrome("Satan, oscillate my metallic sonatas"))
    print(new_palindrome("I roamed under it as a tired nude Maori"))
    print(new_palindrome("Rise to vote sir"))
    print(new_palindrome("Dammit, I'm mad!"))
