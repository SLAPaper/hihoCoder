from math import ceil

z, y, x = sorted(int(x) for x in raw_input().split())
if x <= y + z:
    print int(ceil((x + y + z) / 20.0)) * 6
else:
    run = (y + z) / 10
    xr = x - 10 * run
    nxr = (y + z) % 10
    xr -= 15 - nxr if nxr < 8 else nxr
    print int(run + 1 + ceil(xr / 15.0)) * 6
