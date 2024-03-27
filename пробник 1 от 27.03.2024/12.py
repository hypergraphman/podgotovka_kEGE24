for n in range(4, 100):
    line = '2' + '5' * n
    while '25' in line or '355' in line or '555' in line:
        if '25' in line:
            line = line.replace('25', '5', 1)
        if '355' in line:
            line = line.replace('355', '52', 1)
        if '555' in line:
            line = line.replace('555', '3', 1)
    if line.count('3') == 2:
        print(n)
        break