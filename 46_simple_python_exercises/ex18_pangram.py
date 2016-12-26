#!/usr/bin/env python

"""A pangram is a sentence that contains all the letters of the English alphabet
at least once, for example:
The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a
pangram or not."""

def cleanup(inp_str):
    import re
    pattern = '[^a-z]'
    return re.sub(pattern,'',inp_str)

def is_pangram(inp_str):
    mod_inp_str = [char for char in set(cleanup(inp_str.lower()))]
    if (len(mod_inp_str) == 26):
        return True
    return False

if __name__ == '__main__':
    inp_str = "The quick brown fox jumps over the lazy dog"
    print(is_pangram(inp_str))
    inp_str = "This is a, fun.3454"
    print(is_pangram(inp_str))
    inp_str = "---ABCDEFGHIJKLMNOPQRSTUVWXYZ,034543."
    print(is_pangram(inp_str))

    
