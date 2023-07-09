n = int(input())
v = [None] * 100100

for i in range(1, n+1):
    v[i] = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(100100)]

for i in range(1, n+1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + v[i][j])

print(max(dp[n]))
