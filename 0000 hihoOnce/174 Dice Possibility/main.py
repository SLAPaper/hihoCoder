from __future__ import print_function, division
from fractions import Fraction

import sys


def calc(n, m):
    s = [Fraction()] * (m + 1)
    s[1:6] = [Fraction(1, 6)] * 6
    for i in range(1, n):
        ns = s[:]
        for j in range(1, m + 1):
            ns[j] = ((s[j - 1] if j - 1 > 0 else Fraction()) -
                     (s[j - 7] if j - 7 > 0 else Fraction())) / 6 + ns[j - 1]
        s = ns
    return s[m]


def main():
    n, m = (int(x) for x in raw_input().split())
    sys.stdin.flush()
    print("%.2f" % float(calc(n, m) * 100))


if __name__ == '__main__':
    main()
