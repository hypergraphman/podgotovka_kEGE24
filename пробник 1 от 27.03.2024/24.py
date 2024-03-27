s = open('24.txt').read().strip()
line = s[0]
mx_line = line
for el in s[1:]:
    if line[-1] in 'XZ' and el == 'Y' or line[-1] == 'Y' and el in 'XZ':
        line += el
    else:
        line = el
    if len(line) > 3 and 'XYZY' == line[-4:]:
        line = 'YZY'
    if len(line) > len(mx_line):
        mx_line = line
print(mx_line)
print(len(mx_line))
