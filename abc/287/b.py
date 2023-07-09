N, M = map(int, input().split())

S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0

for s in S:
    flg = False
    for t in T:
        if s.endswith(t):
            flg = True
    if flg:
        ans += 1


print(ans)
