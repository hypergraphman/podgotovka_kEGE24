f = open('27B.txt')
f.readline()
data = [int(x) for x in f]
k = 0
for el in data:
    if el % 5 == 0:
        k += 1
print(k)
# print(data[:10])
# print(data[3:])
print(sum(data[3:]))
# print(data[-10:])
# print(data[:-1])
print(sum(data[:-1]))