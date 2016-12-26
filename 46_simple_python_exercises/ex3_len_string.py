#!usr/bin/env python

#Define a function that computes the length
#of a given list or string.
#(It is true that Python has the
#built in, but writing it yourself
#is nevertheless a good exercise.)

def length(my_string):
    """ this function returns the lenght of a string"""
    print("Input String:", my_string)
    length = 0
    for char in my_string:
        length += 1
    return length

if __name__ == '__main__':
    print(length("This is a test string"))
    print(length(""))
    print(length("Sasidhar"))
