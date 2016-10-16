from lib import rit_lib


class test(rit_lib.struct):
    _slots = ((str, 'f'), (int, 's'))


gg = test('test1', 2)


def main():
    pass


main()
