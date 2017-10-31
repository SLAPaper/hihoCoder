from __future__ import print_function, division
from fractions import Fraction
import sys


def cache(func):
    memory = {}

    def wrapper(n, m):
        if (n, m) in memory:
            return memory[(n, m)]
        else:
            result = func(n, m)
            memory[(n, m)] = result
            return result

    return wrapper


@cache
def calc(n, m):
    if m <= 0:
        return Fraction()

    if n == 1:
        if m in set([1, 2, 3, 4, 5, 6]):
            return Fraction(1, 6)
        else:
            return Fraction()

    n1m1 = calc(n - 1, m - 1)
    nm1 = calc(n, m - 1)
    n1m7 = calc(n - 1, m - 7)

    return (n1m1 - n1m7) / 6 + nm1


def main():
    n, m = (int(x) for x in raw_input().split())
    sys.stdin.flush()
    print("%.2f" % float(calc(n, m) * 100))


if __name__ == '__main__':
    main()
