N = int(input())
P = [0] + list(map(int, input().split()))
S = sum(P)

# 埋める配列: i問目まで解いたとき、得点は何通りあるか？
dp = [[False] * (S + 1) for i in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        mark = dp[i-1][j]
        mark |= P[i] == j
        if j - P[i] >= 0:
            mark |= dp[i-1][j-P[i]]
        dp[i][j] = mark

print(sum(dp[N]))