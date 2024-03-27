def n_to_p(n, p=5):
    alp = '01234'
    r = ''
    while n:
        r = alp[n % p] + r
        n //= p
    return r


def f(n):
    s1 = n_to_p(n)
    if n % 2 == 0:
        s2 = s1 + n_to_p(sum(map(int, s1[-2:])))
    else:
        s2 = s1[-1] + s1
    return int(s2, 5)


for i in range(101, 1000):
    if f(i) > 1000:
        print(i)
        break