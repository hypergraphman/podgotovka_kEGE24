for x in range(15):
    a = int('99658029', 15) + x * 15**2
    b = int('1020023', 15) + x * 15**3
    s = a + b
    if s % 14 == 0:
        print(x, s // 14)