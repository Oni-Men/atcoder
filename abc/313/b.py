N, M = map(int, input().split())

s = set(range(1, N + 1))

for i in range(M):
    a, b = map(int, input().split())
    s.discard(b)

if len(s) == 1:
    print(*s)
else:
    print(-1)
