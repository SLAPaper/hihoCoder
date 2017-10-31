from __future__ import print_function, division
from fractions import Fraction


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
    if n == 1:
        if m in set([1, 2, 3, 4, 5, 6]):
            return Fraction(1, 6)
        else:
            return Fraction()

    r1 = calc(n - 1, m - 1)
    r2 = calc(n - 1, m - 2)
    r3 = calc(n - 1, m - 3)
    r4 = calc(n - 1, m - 4)
    r5 = calc(n - 1, m - 5)
    r6 = calc(n - 1, m - 6)

    return (r1 + r2 + r3 + r4 + r5 + r6) / 6


def main():
    n, m = (int(x) for x in raw_input().split())
    print("%.2f" % float(calc(n, m) * 100))


if __name__ == '__main__':
    main()
