from __future__ import print_function

from ctypes import c_int

BASE = int(1e9 + 7)


class TreeMatrix:
    def __init__(self, N):
        self.mat = (c_int * ((N + 1) * (N + 1)))()
        self.N = N

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def add(self, x, y, val):
        x, y = x + 1, y + 1

        i = x
        while i <= self.N:
            j = y
            while j <= self.N:
                self.mat[i * (self.N + 1) + j] += val
                j += self.lowbit(j)
            i += self.lowbit(i)

    def _sum(self, x, y):
        x, y = x + 1, y + 1
        ret = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                ret += self.mat[i * (self.N + 1) + j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return ret

    def sum(self, x1, y1, x2, y2):
        return (self._sum(x2, y2) - self._sum(x1 - 1, y2) -
                self._sum(x2, y1 - 1) + self._sum(x1 - 1, y1 - 1)) % BASE


if __name__ == '__main__':
    N, M = (int(x) for x in raw_input().split())

    tmat = TreeMatrix(N)

    for _ in range(M):
        op, param = raw_input().split(None, 1)
        if op == 'Add':
            x, y, val = (int(x) for x in param.split())
            tmat.add(x, y, val)
        elif op == 'Sum':
            x1, y1, x2, y2 = (int(x) for x in param.split())
            print(tmat.sum(x1, y1, x2, y2))
