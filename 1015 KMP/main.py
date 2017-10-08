from __future__ import print_function


def _get_next(pattern):
    # type (str) -> List[int]
    next_ = [-1]
    i = 0
    j = -1
    m = len(pattern)
    while i < m - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            next_.append(j)
        else:
            j = next_[j]

    return next_


def kmp_count(original, pattern):
    # type: (str, str) -> int

    n = len(original)
    m = len(pattern)

    i = 0
    j = 0
    count = 0
    next_ = _get_next(pattern)
    while i < n:
        if original[i] == pattern[j]:
            if j == m - 1:
                count += 1
                j = next_[j]
            else:
                i += 1
                j += 1
        else:
            j = next_[j]

        if j == -1:
            i += 1
            j = 0

    return count


N = int(raw_input())

for _ in range(N):
    p = raw_input()
    o = raw_input()
    print(kmp_count(o, p))
