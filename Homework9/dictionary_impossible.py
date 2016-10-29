"""
file: dictionary_impossible.py
language: python 3
author: Duc Phan - ddp3945@rit.edu
description: Implemetation for Homework 9 - CSCI-141
"""


def encode(plaintext, key):
    """
    Encode the plaintext using the key file
    :param plaintext: str
    :param key: str
    :return: python list of str
    """
    print('Preparing to encode {} using {}'.format(plaintext, key))

    d = dict()
    for line in open(key):
        lst = line.strip().split()
        d[lst[0]] = lst[1]
    print('The <word, encoded_word> pair', end='')
    if len(d) <= 1:
        print(' is:')
    else:
        print('s are:')
    print(d)

    ans = []
    for line in open(plaintext):
        lst = line.strip().split()
        s = ''
        for i in range(len(lst)):
            if i > 0:
                s += ' '
            if lst[i] in d:
                s += d[lst[i]]
        ans.append(s)

    return ans


def decode(encoded, key):
    """
    Decode the text using the key file
    :param encoded: python list of str
    :param key: str
    :return: NoneType
    """
    print('The encoded lines are:')
    print(encoded)

    print('The agent is decoding the lines.')
    d = dict()
    for line in open(key):
        lst = line.strip().split()
        d[lst[1]] = lst[0]
    print('The <encoded_word, word> pair', end='')
    if len(d) <= 1:
        print(' is:')
    else:
        print('s are:')
    print(d)

    for line in encoded:
        lst = line.strip().split()
        s = ''
        for i in range(len(lst)):
            if i > 0:
                s += ' '
            if lst[i] in d:
                s += d[lst[i]]
        print(s)


def simulate():
    """
    - Prompt user for a key file and a plain text file
    - Simulate the encoding and decoding process using a key file and a plain text file
    :return: NoneType
    """
    key = input('Enter the name of the secret key file: ')
    plaintext = input('Enter the name of the plain text file: ')
    encoded = encode(plaintext, key)
    print(encoded)
    print('Sending the encoded lines to the agent.')
    decode(encoded, key)


def main():
    print('Welcome to the Encoder 2000!')
    simulate()
    print('Exiting the Encoder 2000!')


main()
