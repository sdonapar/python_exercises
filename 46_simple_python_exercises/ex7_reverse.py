#!/usr/bin/env python

#Define a function reverse() that computes the reversal of a string.
#For example, reverse("I am testing")
#should return the string "gnitset ma I" .

def reverse(inp_string):
    """ this gives the reverse of given string
        reverse(string) -> (string)
    """
    print("Input string:",inp_string)
    start_pos = -1
    end_pos = len(inp_string)*start_pos
    pos = start_pos
    reverse_string = ''
    while (pos >= end_pos):
        reverse_string += inp_string[pos]
        pos += -1
    return reverse_string

if __name__ == '__main__':
    print(reverse("I am testing"))
    print(reverse("Python is awesome"))
