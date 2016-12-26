#!/usr/bin/env python

""" Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words."""

def map_words(word_list):
    """this function returns a list of lenghts for a given list of words
       word_list(list) - > list
    """
    print("Input words list:",word_list)
    word_length = []
    for word in word_list:
        word_length.append(len(word))
    return word_length

def map_words_map(word_list):
    """this function returns a list of lenghts for a given list of words
       word_list(list) - > list
    """
    print("Input words list:",word_list)
    return map(len,word_list)

def map_words_lc(word_list):
    """this function returns a list of lenghts for a given list of words
       word_list(list) - > list
    """
    print("Input words list:",word_list)
    return [len(word) for word in word_list]

if __name__ == '__main__':
    word_list = ['aaa','cc','ddddddd','e']
    print(map_words(word_list))
    print(map_words_map(word_list))
    print(map_words_lc(word_list))
