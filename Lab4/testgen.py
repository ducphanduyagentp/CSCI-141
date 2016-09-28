import random

cmd = ['<', '>', 'S', 'T', 'C', 'F', 'B', 'U', 'D', 'R', 'P', 'G', 'Z']


def main():
    n = int(input())
    while n > 0:
        n = n - 1
        p = random.randint(0, len(cmd) - 1)
        if cmd[p] == 'U' or cmd[p] == 'D':
            print(cmd[p], end='')
        if cmd[p] == 'S' or cmd[p] == 'T' or cmd[p] == 'C' or cmd[p] == 'F' or cmd[p] == 'B':
            num = random.randint(0, 250)
            print(cmd[p], num, sep='', end='')
        if cmd[p] == '<' or cmd[p] == '>':
            num = random.randint(0, 360)
            print(cmd[p], num, sep='', end='')
        if cmd[p] == 'Z':
            num = random.randint(0, 8)
            print(cmd[p], num, sep='', end='')
        if cmd[p] == 'R':
            print(cmd[p], end='')
            num = random.randint(0, 250)
            print(num, ',', sep='', end='')
            num = random.randint(0, 250)
            print(num, end='')
        if cmd[p] == 'P':
            print(cmd[p], end='')
            num = random.randint(0, 15)
            print(num, ',', sep='', end='')
            num = random.randint(0, 100)
            print(num, end='')
        if cmd[p] == 'G':
            print(cmd[p], end='')
            num = random.randint(0, 200)
            print(num, ',', sep='', end='')
            num = random.randint(0, 200)
            print(num, end='')


main()
