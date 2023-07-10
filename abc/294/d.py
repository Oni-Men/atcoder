N, Q = map(int, input().split())

s = set() # 受付に行った人
ans = 1

for _ in range(Q):
  e = list(map(int, input().split()))
  if e[0] is 1:
    pass
  elif e[0] is 2:
    s.add(e[1])
  elif e[0] is 3:
    while ans in s:
      ans += 1
    print(ans)
