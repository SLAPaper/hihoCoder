from __future__ import print_function


def _get_next(pattern, allow_overflapping=False):
    # type (str) -> List[int]
    next_ = [-1]
    i = 0
    j = -1
    while i < len(pattern) - 1:
        if j == -1 or pattern[i] == pattern[j]:
            i += 1
            j += 1
            if not allow_overflapping and pattern[i] == pattern[j]:
                # skip ahead
                next_.append(next_[j])
            else:
                next_.append(j)
        else:
            j = next_[j]

    return next_


def kmp_count(original, pattern, allow_overflapping=True):
    # type: (str, str) -> int

    i = 0
    j = 0
    count = 0
    next_ = _get_next(pattern, allow_overflapping)
    while i < len(original) and j < len(pattern):
        if j == -1 or original[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next_[j]

        if j == len(pattern):
            count += 1
            j = next_[j - 1] + 1

    return count


N = int(raw_input())

for _ in range(N):
    p = raw_input()
    o = raw_input()
    print(kmp_count(o, p))
