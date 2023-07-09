T = int(input())
test = [list(map(int, input().split())) for _ in range(T)]

def solve(n, d, k):
  tiles = [False] * n
  mark = 0
  tiles[mark] = True
  x = (mark + d) % n
  while tiles[x]:
    x = (x + 1) % n
  tiles[x] = True
  mark = x

for i in range(T):
  print(solve(test[i]))