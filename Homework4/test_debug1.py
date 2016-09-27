"""
This program contains a function to
compute the square root
of a non-negative integer without
using a built-in sqrt() function.

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

File:  test_debug1.py
Author: Aaron Deever
Author: Duc Duy Phan - ddp3945@rit.edu

"""


def root(x):
    """
    This function computes the square root of an integer
    without using a built-in sqrt() function.  The technique
    is similar to long division.  Only the integer
    portion of the square root is computed.
    PRECONDITION:  x is integer and x >= 0.
    The function simply returns (None) if x < 0.
    :param x: the value to take the square root of
    :return: the root, truncated to just the integer
    portion of the root.
    """

    if x < 0:
        return

    # determine how many digits are in the number
    digits = 0
    val = x
    while val > 0:
        val = val // 10  # dividing by 10 effectively removes a low-order digit
        digits += 1

    # digits processed in pairs; consider number has a 0
    # in front if necessary to make number of digits even
    if digits % 2 == 1:
        digits += 1

    # go through digits two at a time
    pairsRemaining = digits / 2
    ans = 0
    remainder = 0

    while pairsRemaining > 0:
        # bring down next two digits
        remainder = 100 * remainder + nextTwoDigits(pairsRemaining, x)

        # compute the next digit of the answer
        d = nextAnswerDigit(ans, remainder)

        # use this digit and update the remainder
        remainder = updateRemainder(ans, remainder, d)

        # update current answer based on new digit
        ans = 10 * ans + d

        pairsRemaining -= 1

    return ans


def nextTwoDigits(pairsRemaining, x):
    """
    Grabs the next two highest order digits that
    haven't yet been processed.
    :param pairsRemaining: how many pairs of digits have not yet
    been processed
    :param x: original number
    :return: the two digits as a two-digit number
    """

    # skip over low order pairs of digits
    pairsToSkip = pairsRemaining - 1
    a = 1
    while pairsToSkip > 0:
        x = x // 100  # dividing by 100 removes a low-order pair of digits
        a = a * 100
        pairsToSkip -= 1

    # Bug fixed: after remove the low-order pairs of digits, we still need to extract
    # the necessary pair of digits
    x = x % 100

    # grab and return the next pair as 2-digit number
    return x


def nextAnswerDigit(currentAnswer, remainder):
    """
    computes the next digit of the answer based on the
    currentAnswer and the current remainder.
    :param currentAnswer: answer so far
    :param remainder: remainder so far
    :return: the next digit of the answer
    """

    # first we double the currentAnswer
    currentAnswer *= 2

    # then we want the largest digit, d, such that
    # current answer with d added as a last digit, then
    # multiplied by d, is less than or equal to the current remainder

    d = 9
    while d >= 0:
        product = (10 * currentAnswer + d) * d
        if product <= remainder:
            return d
        d -= 1


def updateRemainder(currentAnswer, remainder, newDigit):
    """
    Based on the new answer digit just calculated, this
    function computes the new remainder.  (Really this
    could be folded into the nextAnswerDigit function,
    which could return the new digit and the new remainder,
    but we haven't discussed how to have a function
    return multiple values yet.)
    :param currentAnswer: answer so far
    :param remainder: remainder so far
    :param newDigit: new digit to be appended to current answer
    :return:
    """

    currentAnswer *= 2
    product = (10 * currentAnswer + newDigit) * newDigit
    return remainder - product


def testRoot():
    # Perfect Squares with different numbers of digits
    print(root(0) == 0)
    print(root(4) == 2)
    print(root(16) == 4)
    print(root(81) == 9)
    print(root(100) == 10)
    print(root(1024) == 32)
    print(root(1000000) == 1000)  # 10e6
    print(root(100000000) == 10000)  # 10e8

    # Different inputs with the same integer output
    print(root(1024) == 32)
    print(root(1025) == 32)
    print(root(1035) == 32)
    print(root(1060) == 32)
    print(root(1080) == 32)
    print(root(1088) == 32)

    print(root(100) == 10)
    print(root(102) == 10)
    print(root(110) == 10)
    print(root(120) == 10)

    print(root(81) == 9)
    print(root(85) == 9)
    print(root(89) == 9)
    print(root(97) == 9)

    print(root(1) == 1)
    print(root(2) == 1)
    print(root(3) == 1)


testRoot()
