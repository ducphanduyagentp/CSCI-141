"""
file: text_count.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Homework 3 - CSCI-141
"""

import pdb


def count_text_string(search_for, search_in):
    """Counts and return the number of occurences of the string search_for in the string search_in"""
    if len(search_for) > len(search_in):
        return 0
    if search_for == '':
        return 0
    s1 = ''
    s2 = search_in
    sum = 0
    pdb.set_trace()
    for i in range(len(search_for)):
        s1 = s1 + s2[0]
        s2 = s2[1:]
    if search_for == s1:
        sum = 1
    return sum + count_text_string(search_for, search_in[1:])


def count_text_file(search_for, text_file_name):
    """
    - Count and return the number of occurrences of string search_for in file text_file_name
    - Print the lines in the file text_file_name that contain the string search_for
    """
    asum = 0
    for lines in open(text_file_name):
        sum = count_text_string(search_for, lines)
        asum = asum + sum
        if sum > 0:
            print(lines.rstrip())
    return asum


def main():
    """
    - Prompt users for a string to search for
    - Prompt users for a filename to search in
    - Print the lines in the file which contain the input string
    - Print the number of occurrences of the input string in the file
    """
    search_for = input('Enter text:')
    text_file_name = input('Enter filename:')
    sum = count_text_file(search_for, text_file_name)
    print('Total count of', search_for, 'is:', sum, sep=' ')


main()
