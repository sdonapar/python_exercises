#!/usr/bin/env python

#Define a function overlapping() that takes two lists and returns True
#if they have at least one member in common,
#False otherwise. You may use your is_member() function,
#or the in operator, but for the sake of the exercise, you
#should (also) write it using two nested for-loops.

from ex8_is_member import is_member

def overlapping(list1,list2):
    """ this check if there any overlapping element in given 2 lists
        overlapping(list,list) -> bool
    """
    print("Input list1:",list1)
    print("Input list2:",list2)

    for elem1 in list1:
        if is_member(elem1,list2):
            return True
        return False
if __name__ == '__main__':
    print(overlapping(['a','b','c'],['x','y','z','a']))
    print(overlapping(['a','b','c'],['x','y','z']))
        
