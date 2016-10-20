from slList_stu import *


def main():
    lst = createList()
    for i in range(7):
        append(lst, i)
    print(lst)
    copySegment(lst, 3, 3)
    print(lst)


main()
