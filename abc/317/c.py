import itertools

N, M = map(int, input().split())
W = [[-1] * N for _ in range(N)]

for i in range(M):
  a, b, c = map(int, input().split())
  W[a - 1][b - 1] = c
  W[b - 1][a - 1] = c

ans = 0

for p in itertools.permutations(range(N)):
  length = 0
  for i in range(N-1):
    segment = W[p[i]][p[i+1]]
    if segment < 0:
      break
    length += segment
  ans = max(ans, length)

print(ans)