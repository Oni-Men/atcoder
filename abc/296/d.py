from math import ceil


N, M = map(int, input().split())
INF = 10 ** 18

ans = INF
for a in range(1, N+1):
    b = ceil(M / a)
    if b <= N:
        ans = min(ans, a * b)
    if a > b:
        break

print(ans if ans != INF else -1)
