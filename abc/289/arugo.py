N = int(input())

DP = [0] * (N + 1)

DP[0] = 1
DP[1] = 1

for i in range(2, N + 1):
  DP[i] = DP[i - 2] + DP[i - 1]

print(DP[-1])