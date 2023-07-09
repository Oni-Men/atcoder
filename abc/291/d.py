N = int(input())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

# dp[i][x] := i枚目まで選べて、そのときの表(x=0)と裏(x=1)を選んだ時の条件を満たす個数
dp = [1, 1]
for i in range(N-1):
    next = [0, 0]
    if A[i] != A[i + 1]:
        next[0] += dp[0]
    if A[i] != B[i + 1]:
        next[1] += dp[0]
    
    if B[i] != A[i + 1]:
        next[0] += dp[1]
    if B[i] != B[i + 1]:
        next[1] += dp[1]

    next[0] %= 998244353
    next[1] %= 998244353
    dp = next

print(sum(dp) % 998244353)