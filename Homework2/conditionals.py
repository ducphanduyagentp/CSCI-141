"""
file: conditionals.py
language: python 3
author: Duc Duy Phan - ddp3945@rit.edu
description: Homework 2 - Conditionals
"""


def divisible(a, b):
    """
       - Input: 2 integers
       - Determine if the larger integer is evenly divisible by the smaller integer.
       - Inform users if the inputs contain non-positive integers.
       - Inform users if the inputs are both positive and equal.
    """
    if a <= 0 or b <= 0:
        print("Inputs must be positive integers!")
    elif a == b:
        print("Those integers are equal:", a)
    else:
        if a < b:
            a, b = b, a
        if a % b == 0:
            print(a, "is evenly divisible by", b)
        else:
            print(a, "is not evenly divisible by", b)


def test_divisible():
    """
    This function provides different input sets for the function 'divisible'
    """
    # Negative and equal integers
    divisible(-1, -1)
    # Zero and zero
    divisible(0, 0)
    # Negative and inequal integers
    divisible(-1, -2)
    # Negative integer and zero
    divisible(-1, 0)
    # Negative and positive integers
    divisible(-1, 2)
    # Positive and equal integers
    divisible(69, 69)
    # Positive integers
    divisible(11111, 11)
    divisible(122112211221, 3)
    divisible(3, 14)
    divisible(3, 15)
    divisible(15, 3)
    divisible(3, 9)
    divisible(10000000007, 17)


def triangle(a, b, c):
    """
       - Input: 3 integers a, b and c
       - Inform users if all the inputs are not positive integers
       - Determine if the 3 integers in the input can be the lengths of the sides of a triangle
    """
    if (a <= 0 or b <= 0 or c <= 0):
        print("Triangles require sides of positive length!")
    elif (a + b >= c and a + c >= b and b + c >= a):
        print(a, ",", b, "and", c, "can form a triangle")
    else:
        print(a, ",", b, "and", c, "can not form a triangle")


def test_triangle():
    """
    This function provides different input sets for the function 'triangle'
    """
    # Same parameters but in different orders
    triangle(1, 2, 3)
    triangle(3, 2, 1)
    triangle(1, 3, 2)
    # Input includes non-positive integer(s)
    triangle(0, 1, 1)
    triangle(-1, 2, 1)
    triangle(-1, -1, -1)
    triangle(-1, -2, -3)

    # Random inputs
    triangle(1, 2, 4)
    triangle(44, 11, 123)
    triangle(11, 11, 22)
    triangle(14, 15, 16)
    triangle(3, 4, 5)


def main():
    """Call the test_divisible function and the test_triangle function"""
    test_divisible()
    test_triangle()


main()
