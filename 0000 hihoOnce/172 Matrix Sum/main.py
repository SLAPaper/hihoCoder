from __future__ import print_function

from array import array
import sys


class TreeMatrix:
    def __init__(self, N, M):
        self.mat = [array('i', [0] * (M + 1))] * (N + 1)
        self.N = N
        self.M = M

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def add(self, x, y, val):
        i = x
        while i <= self.N:
            j = y
            while j <= self.M:
                print(i, j, val)
                print(self.mat)
                self.mat[i][j] += val
                j += self.lowbit(j)
            i += self.lowbit(i)

    def _sum(self, x, y):
        ret = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                ret += self.mat[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return ret

    def sum(self, x1, y1, x2, y2):
        return self._sum(x1 - 1, y1 - 1) - self._sum(x1 - 1, y2) - self._sum(
            x2, y1 - 1) + self._sum(x2, y2)


def main(stdin=sys.stdin):
    sys.stdin = stdin

    N, M = (int(x) for x in raw_input().split())

    tmat = TreeMatrix(N, N)

    for _ in range(M):
        op, param = raw_input().split(None, 1)
        if op == 'Add':
            x, y, val = (int(x) for x in param.split())
            tmat.add(x + 1, y + 1, val)
        elif op == 'Sum':
            x1, y1, x2, y2 = (int(x) for x in param.split())
            print(tmat.sum(x1 + 1, y1 + 1, x2 + 1, y2 + 1))


main()
