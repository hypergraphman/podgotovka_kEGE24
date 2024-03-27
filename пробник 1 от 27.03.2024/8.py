from itertools import product

words = [''.join(word) for word in product(sorted('гондубш'), repeat=6)]
ans = 0
for i, word in enumerate(words, start=1):
    if i % 2 and word[0] != 'б' and word.count('н') >= 2 and 'у' not in word:
        ans = i
print(ans)