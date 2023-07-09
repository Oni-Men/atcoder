N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

DP = [0] * (X + 1)
DP[0] = 1

for i in range(1, X + 1):
  if i in B:
    continue
  for k in range(N):
    j = i - A[k]
    if j < 0: continue
    if DP[j]:
      DP[i] = 1
      break

if DP[X]:
  print("Yes")
else:
  print("No")
