from collections import deque

n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a = deque(a)
b = deque(b)

ans = -1

while True:
    if len(a) == 0 or len(b) == 0:
        ans = -1
        break
    if abs(a[-1] - b[-1]) <= d:
        ans = a[-1] + b[-1]
        break
    else:
        if a[-1] > b[-1]:
            a.pop()
        else:
            b.pop()

print(ans)
