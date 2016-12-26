#!/usr/bin/env python

#Define a function max() that takes two numbers
#as arguments and returns the largest of them.
#Use the if-then-else construct available in Python.
#(It is true that Python has the max()
#function built in, but writing it
#yourself is nevertheless a good exercise.)

def my_max(a,b):
    """ this funcition returns max of 2 numbers"""
    print("input numbers : ", a, b)
    max = a
    if (b > max):
        max = b
    return max

if __name__ == '__main__':
    print(my_max(10,20))
    print(my_max(30,35))
    print(my_max(30.1,30))
    print(my_max(0,0))
    print(my_max(10,10))
