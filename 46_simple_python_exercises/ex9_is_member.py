#!/usr/bin/env python

#Write a function is_member() that takes a value
#(i.e. a number, string, etc) x and a list of values a , and returns True
#if x is a member of a , False otherwise. (Note that this is exactly what the in operator does, but for the sake of the
#exercise you should pretend Python did not have this operator.)

def is_member(inp_str,inp_list):
    """ this checks the membership of a given string in a list
        is_member(str,list) -> bool
    """
    print("Input string and list:",inp_str,inp_list)
    
    for member in inp_list:
        if member == inp_str:
            return True
    return False

if __name__ == '__main__':
    print(is_member("a",['a','b','c','d']))
    print(is_member(20,[1,2,3,5,20]))
    print(is_member('x',['p','q','r',10,30]))
    print(is_member(5,['a','x','y',30,40]))
