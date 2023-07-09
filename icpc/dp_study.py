N, W = map(int, input().split())
w = [0] * N
v = [0] * N

for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[-1] * (W+1) for _ in range(N+1)]


def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    ans = 0
    if i == N:
        ans = 0
    elif j < w[i]:
        ans = dfs(i + 1, j)
    else:
        ans = max(dfs(i+1, j - w[i]) + v[i], dfs(i+1, j))
    dp[i][j] = ans
    return ans


print(dfs(0, W))
