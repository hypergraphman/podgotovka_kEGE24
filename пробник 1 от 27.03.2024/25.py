from fnmatch import fnmatch
from functools import lru_cache


@lru_cache(None)
def m(k):
    for d in range(2, int(k**0.5) + 1):
        if k % d == 0:
            return d + k // d
    return 0


for k in range(512034, 10**8, 2):
    if m(k) != 0 and m(k) % 117 == 0 and fnmatch(str(k), '51*2?34'):
        print(k, m(k), sep='\t')