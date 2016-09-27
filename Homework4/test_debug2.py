"""
This program contains a function that
determines whether or not it is possible
to take a string (of lowercase English letters),
and without changing the relative order or the
characters in the string, partition the characters
into two substrings that are each in alphabetical
order.

For example, given the original string: "chbke",
it is possible to partition the characters as desired:
"chk" and "be".  Each substring
is in alphabetical order, and the characters are in
the same relative order as the original string (e.g. 'k'
comes after 'c' in substring 1, so it must also have been
in that order in the original string).

As another example, the original string: "gjba"
can not be split is desired.

Duplicate characters are allowed, and are considered
to be in alphabetical order.  For example, the original
string: "fmcmh" can be split into "fmm" and "ch".

It has bug(s).

There are no tests (yet).

Your job is to
1) include in this program a sufficient
suite of pass/fail tests to thoroughly
test the function and expose all error(s).

2) Generate a screenshot that
demonstrates your use of a debugger
to step through the function. Specifically it should
illustrates the execution point of a test at
which the function makes (or is about to make)
a mistake.

3) fix the code and document your fix(es).
Include additional tests if you feel it
necessary to thoroughly test the function.

You will submit your updated version of this
file (along with a separate document containing
the screenshot and answered questions).

File:  test_debug2.py
Author: Aaron Deever
Author: Duc Duy Phan - ddp3945@rit.edu
"""


def alphaSplit(inputString):
    # go through the characters, one by one, and
    # place the character at the end of a substring
    # if possible.  If the character could extend
    # both substrings, always prefer the substring
    # whose current last character is closest alphabetically
    # to the one being placed (i.e. prefer to 'use up'
    # as little space as possible).

    sub1 = ""
    sub2 = ""

    for idx in range(len(inputString)):  # Bug #1 fixed
        currCh = inputString[idx]

        if idx == 0:  # first character can always go in sub1
            sub1 = currCh

        elif len(sub2) == 0:  # use sub1 if valid, uses up less space
            if sub1[-1] <= currCh:
                sub1 = sub1 + currCh
            else:
                sub2 = currCh

        else:
            # both substrings have characters.
            # Return false if neither option is valid.
            # Otherwise, choose the valid
            # option that uses up less space.
            if sub1[-1] > currCh and sub2[-1] > currCh:  # Bug #2 fixed
                # can't be placed, neither option valid; return false
                return False
            elif sub1[-1] < sub2[-1]:
                # sub2[-1] is later in the alphabet, so use sub2 if possible
                # because it will use up less space
                if sub2[-1] <= currCh:
                    sub2 = sub2 + currCh
                else:
                    sub1 = sub1 + currCh
            else:
                # same idea with substring roles reversed
                if sub1[-1] <= currCh:
                    sub1 = sub1 + currCh
                else:
                    sub2 = sub2 + currCh

    # made it to the end so must be True
    return True


def testAlphaSplit():
    # String contains only 1 type of character
    print(alphaSplit('aaaaaaaaaa') == True)
    print(alphaSplit('bbbbbb') == True)
    print(alphaSplit('ddddd') == True)
    print(alphaSplit('eeeeeeeeeeeeeeeeeeeeeeee') == True)

    # String with 2 types of character and alternating each other
    print(alphaSplit('ababababababababababababab') == True)
    print(alphaSplit('cdcdcdc') == True)
    print(alphaSplit('aza') == True)

    # String in reversing alphabet order
    print(alphaSplit('dcba') == False)
    print(alphaSplit('zy') == True)
    print(alphaSplit('zya') == False)
    print(alphaSplit('fedcba') == False)

    # Others
    print(alphaSplit('chbke') == True)
    print(alphaSplit('fmcmh') == True)
    print(alphaSplit('abfcege') == True)


testAlphaSplit()
