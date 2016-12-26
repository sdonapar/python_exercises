#!/usr/bin/env python

"""Write a function filter_long_words() that takes a list of words and
returns the list of words that are longer than n, an integer"""

def filter_long_words(word_list,n):
    """this function returns list of words that longer than n"""
    print("inpit word list:",word_list)
    return [word for word in word_list if len(word) > n]

if __name__ == '__main__':
    print(filter_long_words(['aaa','def','eeee','gg'],3))



