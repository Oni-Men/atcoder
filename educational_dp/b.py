N, K = map(int, input().split())
h = list(map(int, input().split()))

inf = float("inf")
dp = [inf] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    for j in range(1, min(i+1, K+1)):
        value = dp[i-j] + abs(h[i-j] - h[i])
        dp[i] = min(dp[i], value)

print(dp[-1])
