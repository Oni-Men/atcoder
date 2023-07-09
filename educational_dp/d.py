N, W = map(int, input().split())
w, v = [0] * (N+1), [0] * (N+1)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j - w[i] < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i]] + v[i])

print(dp[N][W])
