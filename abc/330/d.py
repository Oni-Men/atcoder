N = int(input())
S = [list(input()) for _ in range(N)]

R = [0] * N # i行目の o の個数
C = [0] * N # j列目の o の個数

for i in range(N):
  for j in range(N):
    if S[i][j] == "o":
      R[i] += 1
      C[j] += 1

ans = 0

for i in range(N):
  for j in range(N):
    r = R[i]
    c = C[j]
    if S[i][j] == "o":
      ans += (r - 1) * (c - 1)


print(ans)
