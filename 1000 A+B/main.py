from __future__ import print_function, division, absolute_import, unicode_literals

while True:
    try:
        # get raw_input and do all the calculation
        m, n = (int(x) for x in raw_input().split())
        print(m + n)
    except EOFError:
        break