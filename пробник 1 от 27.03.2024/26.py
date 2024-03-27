a = [0] * 70
b = [0] * 30

f = open('26.txt')
n = int(f.readline())
data = []
for line in f:
    s, e, t = line.split()
    data.append((int(s), int(e), t))
data.sort()
count_not_park = 0
count_b_park = 0
for s, e, t in data:
    is_park = False
    if t == 'A':
        for i in range(len(a)):
            if a[i] <= s:
                a[i] = s + e
                is_park = True
                break
    if not is_park:
        for i in range(len(b)):
            if b[i] <= s:
                b[i] = s + e
                is_park = True
                break
    if not is_park:
        count_not_park += 1
    if t == 'B' and is_park:
        count_b_park += 1
print(count_b_park, count_not_park)