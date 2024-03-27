def f(c, e):
    if c > e or c == 81:
        return 0
    if c == e:
        return 1
    moves = [
        f(c + int(str(c)[0]), e),
        f(c + 3, e),
        f(2 * c - 1, e)
    ]
    return sum(moves)


print(f(42, 73) * f(73, 89))
