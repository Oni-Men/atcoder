x, y, z = map(int, input().split())
s = input()

# 埋めるDP配列
# i文字目まで入力したときの最短時間 -> len(s)程度の長さが必要
INF = 10 ** 18
dp  = [[INF, INF] for _ in range(len(s) + 1)]
dp[0][0] = 0

for i in range(len(s)):
    if s[i] == "a":
        dp[i+1][0] = min(dp[i][0]+x, dp[i][1]+x+z, dp[i][1]+y+z)
        dp[i+1][1] = min(dp[i][1]+y, dp[i][0]+x+z, dp[i][0]+y+z)
    else:
        dp[i+1][0] = min(dp[i][0]+y, dp[i][1]+x+z, dp[i][1]+y+z)
        dp[i+1][1] = min(dp[i][1]+x, dp[i][0]+z+x, dp[i][0]+y+z)


print(min(dp[len(s)]))