def solve(n, x):
  ans = 0
  for i in range(1, n+1):
    for j in range(i, n+1):
      for k in range(j, n +1):
        if i == j or j == k or k == i:
          continue
        if i + j + k == x:
          ans += 1
  print(ans)

while True:
    n, x = map(int, input().split())
    if x == 0 and n == 0:
      break
    solve(n, x)