N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    a = dp[i - 1] + abs(h[i-1] - h[i])
    b = dp[i - 2] + abs(h[i-2] - h[i])
    if a < b:
        dp[i] = a
    else:
        dp[i] = b

print(dp[-1])
