n, k, q = map(int, input().split())

a = [0] * n

for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    a[x] = y
