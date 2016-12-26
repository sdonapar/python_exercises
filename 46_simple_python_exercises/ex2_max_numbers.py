#!/usr/bin/env python

#Define a function max_of_three()
#that takes three numbers as arguments and
#returns the largest of them.

def my_max(a,b,c):
    """ this funcition returns max of 3 numbers"""
    print("input numbers : ", a, b, c)
    max = a
    if (b > max):
        max = b
    if (c > max):
        max = c
    return max

if __name__ == '__main__':
    print(my_max(10,20,5))
    print(my_max(30,35,55))
    print(my_max(38,32,20))
    print(my_max(30.1,30,30))
    print(my_max(0,0,0))
    print(my_max(10,10,10))
