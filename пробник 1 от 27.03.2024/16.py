def f(n):
    if n <= 2 or n == 8:
        return 0
    if n == 3:
        return 1
    return f(n - 2) + f(n - 1)


for n in range(1, 100):
    if f(n) == 25:
        print(n)