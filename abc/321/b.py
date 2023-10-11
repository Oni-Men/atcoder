N, X = map(int, input().split())
A = list(map(int, input().split()))

s = 0
ok = False

while s <= 100:
  B = sorted(A + [s])
  F = sum(B[1:-1])
  if F >= X:
    ok = True
    break
  s += 1

if not ok or s > 100:
  print(-1)
else:
  print(s)