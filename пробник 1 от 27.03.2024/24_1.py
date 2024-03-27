s = open('24.txt').read().strip()

k = 0
mx = 0
mx_i = 0
for i in range(0, len(s) - 1, 2):
    if k == 1 and s[i] + s[i + 1] == 'ZY' and s[i - 2] + s[i - 1] == 'XY':
        k = 1
    if s[i] in 'XZ' and s[i + 1] == 'Y':
        k += 1
    else:
        k = 0
    if k > mx:
        if k > 0 and s[i] + s[i + 1] == 'ZY' and s[i - 2] + s[i - 1] == 'XY':
            if k - 1 > mx:
                mx = k - 1
                mx_i = i
        else:
            if k > mx:
                mx = k
                mx_i = i
print(mx, s[mx_i - 20:mx_i + 4])

