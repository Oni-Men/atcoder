n = int(input())
a = list(map(int, input().split()))

mark = {}
f = {}

for i in range(len(a)):
    ai = a[i]
    if ai not in mark:
        mark[ai] = 0
    elif mark[ai] == 0:
        f[ai] = i + 1
        mark[ai] += 1

res = [i + 1 for i in range(n)]
res = sorted(res, key=lambda x: f[x])

print(" ".join(map(str, res)))
