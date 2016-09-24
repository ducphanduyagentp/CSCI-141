import turtle as t


def extract_num(s):
    if len(s) == 0 or not s[0].isdigit():
        return None
    for i in range(len(s)):
        if not s[i].isdigit():
            return int(s[:i])
    return int(s)


def processLeft(num):
    t.left(num)


def processRight(num):
    t.right(num)


def processS(num):
    pass


def processT(num):
    pass


def processC(num):
    pass


def processF(num):
    pass


def processB(num):
    pass


def processU():
    pass


def processD():
    pass


def processZ(num):
    pass


def processR(num1, num2):
    pass


def processP(num1, num2):
    pass


def processG(num1, num2):
    pass


def processShapyTurtle(s):
    for i in range(len(s)):
        if s[i] == '<':
            num = extract_num(s[i + 1:])
            processLeft(num)
        elif s[i] == '>':
            num = extract_num(s[i + 1:])
            processRight(num)
        elif s[i] == 'S':
            num = extract_num(s[i + 1:])
            processS(num)
        elif s[i] == 'T':
            num = extract_num(s[i + 1:])
            processT(num)
        elif s[i] == 'C':
            num = extract_num(s[i + 1:])
            processC(num)
        elif s[i] == 'F':
            num = extract_num(s[i + 1:])
            processF(num)
        elif s[i] == 'B':
            num = extract_num(s[i + 1:])
            processB(num)
        elif s[i] == 'U':
            processU()
        elif s[i] == 'D':
            processD()
        elif s[i] == 'R':
            num1 = extract_num(s[i + 1:])
            num2 = 0
            for j in range(i + 1, len(s)):
                if s[j] == ',':
                    num2 = extract_num(s[j + 1:])
                    break
            processR(num1, num2)
        elif s[i] == 'P':
            num1 = extract_num(s[i + 1:])
            num2 = 0
            for j in range(i + 1, len(s)):
                if s[j] == ',':
                    num2 = extract_num(s[j + 1:])
                    break
            processP(num1, num2)
        elif s[i] == 'G':
            num1 = extract_num(s[i + 1:])
            num2 = 0
            for j in range(i + 1, len(s)):
                if s[j] == ',':
                    num2 = extract_num(s[j + 1:])
                    break
            processG(num1, num2)
        elif s[i] == 'Z':
            num = extract_num(s[i + 1:])
            processZ(num)


processShapyTurtle('>123')
t.done()
