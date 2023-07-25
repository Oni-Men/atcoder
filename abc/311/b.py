N, D = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
streak = 0

for j in range(D):
    ok = True
    for i in range(N):
        if S[i][j] == "x":
            ok = False
    if ok:
        streak += 1
    else:
        streak = 0
    ans = max(ans, streak)

print(ans)
