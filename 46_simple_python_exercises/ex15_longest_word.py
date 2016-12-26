#!/usr/bin/env python

"""Write a function find_longest_word() that takes a list of words
and returns the length of the longest one."""

def find_longest_word(word_list):
    """this function retuns the length of largets word in a word list
        find_longest_word(list) -> (number)
    """
    print("Input word list:",word_list)
    return max([len(word) for word in word_list])

if __name__ == '__main__':
    print(find_longest_word(['aaa','cc','longest']))
