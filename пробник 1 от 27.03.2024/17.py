f = open('17.txt')
a = [int(x) for x in f]
mx = 0
for el in a:
    if el % 100 == 47:
        mx = max(mx, el)

b = []
for q in zip(a, a[1:], a[2:], a[3:]):
    if sum([el > 1000 for el in q]) == 2 and sum(q) <= mx:
        b.append(sum(q))
print(len(b), max(b))