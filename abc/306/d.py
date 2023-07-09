INF = 10 ** 18

n = int(input())
x = [0] * (n + 1)
y = [0] * (n + 1)

for i in range(0, n):
    x[i], y[i] = map(int, input().split())

dp = [[-INF, -INF] for _ in range(n + 1)]
dp[0][0] = 0

for i in range(0, n):
    dp[i+1][0] = max(dp[i+1][0], dp[i][0])
    dp[i+1][1] = max(dp[i+1][1], dp[i][1])
    if x[i] == 0:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0]+y[i])
        dp[i+1][0] = max(dp[i+1][0], dp[i][1]+y[i])
    else:
        dp[i+1][1] = max(dp[i+1][1], dp[i][0]+y[i])

print(max(dp[n]))
