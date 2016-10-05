import bsearch
import selection_sort


def main():
    filename = input('Please input file name: ')
    lst = []
    for lines in open(filename):
        lst.extend(lines.split())
    while True:
        s = input('Please enter a word to search for: ')
        if s == '<QUIT>':
            break
        flag = False
        for s1 in lst:
            if s == s1:
                flag = True
                print('The word has been found')
        if not flag:
            print('The word does not exist in the list')


import random
import string


def gen_list():
    nTest = random.randint(0, 100)
    lst = []
    for i in range(nTest):
        nChar = random.randint(0, 50)
        s = ''
        for j in range(nChar):
            s = s + random.choice(string.ascii_letters)
        lst.append(s)
    return lst


def test():
    testMode = 0

    if testMode == 0:
        n = int(input())
        lst = []
        for i in range(n):
            s = input()
            lst.append(s)
        sorted_lst = selection_sort.selectionSort(lst)
        target = input()
        index = bsearch.get_index(sorted_lst, target)
        print(index)
    elif testMode == 1:
        nTest = int(input())
        flag = True
        for i in range(nTest):
            lst = gen_list()
            # print(lst)
            sorted_lst = selection_sort.selectionSort(lst)
            # print(sorted_lst)
            flag1 = True
            for x in string.ascii_letters:
                index = bsearch.get_index(sorted_lst, x)
                index2 = None
                for j in range(len(sorted_lst)):
                    if sorted_lst[j] != '' and sorted_lst[j][0] == x:
                        index2 = j
                        break
                flag1 &= index == index2
            flag &= flag1
        print(flag)


test()
