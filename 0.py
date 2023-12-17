s = input().strip()
n = len(s)
pi = [0]*n

j = 0
for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j
bj= []
k = pi[n - 1]
while k > 0:
    bj.append(k)
    k = pi[k - 1]

if len(bj) > 0:
    print(' '.join(map(str, bj[::-1])))
else:
    print('')