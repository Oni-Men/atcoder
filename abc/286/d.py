n, x = map(int, input().split())
A = [0] * n
B = [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())

MAX = x + 1
dp = [[False] * (MAX) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(0, x+1):
        if dp[i][j]:
            for k in range(B[i]+1):
                if j+A[i]*k < x+1:
                    dp[i+1][j+A[i]*k] = True

print("Yes" if dp[n][x] else "No")
