#!/usr/bin/env python

"""Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")."""

def char_freq(inp_str):
    freq_dict = {}
    for char in inp_str:
        if freq_dict.get(char,None):
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

if __name__ == '__main__':
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))
    print(char_freq("aabbbcdd"))
