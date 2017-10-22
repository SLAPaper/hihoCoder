from __future__ import print_function

N = int(raw_input())
A = [int(x) for x in raw_input().split()]


def prefix_sum(a):
    prev = 0
    for x in a:
        prev += x
        yield prev
    yield prev


S = list(prefix_sum(A)) + [0]

F = [[0] * N for _ in range(N)]

for j_ in range(N):
    i = 0
    j = j_
    while i < N and j < N:
        if i == j:
            F[i][j] = A[i]
        else:
            F[i][j] = S[j] - S[i - 1] - min([F[i + 1][j], F[i][j - 1]])
        i += 1
        j += 1

import sys
sys.stdin.flush()

print(F[0][N - 1])
