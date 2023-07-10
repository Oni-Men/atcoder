Q = int(input())

for _ in range(Q):
  q = input().split()
  if q[0] is "1":
    x = int(q[1])
  elif q[0] is "2":
    pass
  else:
    ans = 0
    print(ans % 998244353)