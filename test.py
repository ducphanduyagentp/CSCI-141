def solve(s):
    lens = len(s)
    i = 0
    while i < lens * 2:
        if s[i] == '[':
            s = s[:i + 1] + ']' + s[i + 1:]
        elif s[i] == ']':
            s = s[:i] + '[' + s[i:]
        elif s[i] == '(':
            s = s[:i + 1] + ')' + s[i + 1:]
        elif s[i] == ')':
            s = s[:i] + '(' + s[i:]
        elif s[i] == '{':
            s = s[:i + 1] + '}' + s[i + 1:]
        elif s[i] == '}':
            s = s[:i] + '{' + s[i:]
        i = i + 2
    return s


def main():
    s = '{{'
    print(solve(s))


main()
