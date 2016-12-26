#!/usr/bin/env python

#Define a function sum()and a function multiply()
#that sums and multiplies (respectively) all the numbers in a list
#of numbers. For example, sum([1, 2, 3, 4]) should return 10 ,
#and multiply([1, 2, 3, 4]) should return 24 .


def sum(my_list):
    """ This function retuns the sum of numbers in a list"""

    print("Input list(sum):",my_list)
    total_sum = 0
    
    for num in my_list:
        total_sum += num
    return total_sum

def multiply(my_list):
    """ This function returns the product of numbers in a list
        multiply(list of numbers) -> (number)
    """
    print("Input list(multiply):",my_list)
    mul_product = 1

    for num in my_list:
        mul_product *= num
    return mul_product

if __name__ == '__main__':
    print(sum([1, 2, 3, 4]))
    print(multiply([1,2,3,4]))
    print(multiply([4,5,0,8]))
