def startsWith(prefix, word):
    return prefix == word[:len(prefix)]


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


main()
