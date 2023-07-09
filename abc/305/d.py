from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
q = int(input())

acc = [0] * (n)
for i in range(1, n):
    acc[i] = acc[i - 1]
    if i % 2 == 0:
        acc[i] += a[i] - a[i - 1]


def f(x):
    i = bisect_left(a, x)
    ret = acc[i]
    if i % 2 == 0:
        ret -= a[i] - x
    return ret


ans = []

for i in range(q):
    l, r = map(int, input().split())
    ans.append(f(r) - f(l))

for i in ans:
    print(i)
