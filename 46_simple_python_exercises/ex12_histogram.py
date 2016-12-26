#!/usr/bin/env python

#Define a procedure histogram() that takes a list of integers
#and prints a histogram to the screen. For example,
#histogram([4, 9, 7]) should print the following:
#****
#*********
#*******

def histogram(num_list,char='*'):
    """ this function prints a histogram based on the list of numbers"""
    print("Input list:",num_list)
    for num in num_list:
        print(char * num)

if __name__ == '__main__':
    histogram([4,9,7])
    histogram([5,5,5])
    histogram([5,8,13],'@')
    
