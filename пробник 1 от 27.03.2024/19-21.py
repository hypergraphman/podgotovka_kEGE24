def f(s1, s2, c, m):
    if s1 + s2 >= 231:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(s1 + 4, s2, c + 1, m),
             f(s1 * 3, s2, c + 1, m),
             f(s1, s2 + 4, c + 1, m),
             f(s1, s2 * 3, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 217 + 1):
    for m in range(1, 4 + 1):
        if f(10, s, 0, m):
            if m == 4:
                print(s, m)
            break