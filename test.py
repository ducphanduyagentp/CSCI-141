def count(filename):
    d = dict()
    for line in open(filename):
        lst = line.strip().split()
        for word in lst:
            if not word in d:
                d[word] = 1
            else:
                d[word] += 1
    lst = list(d.keys())
    lst.sort()
    for word in lst:
        print('{}: {}'.format(word, d[word]))
