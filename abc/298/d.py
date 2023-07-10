from collections import deque
Q = int(input())
S = deque()
S.append(1)

ans = 1

for _ in range(Q):
  q = input().split()
  if q[0] is "1":
    x = int(q[1])
    ans = ans * 10 + x
    ans %= 998244353
    S.append(x)
  elif q[0] is "2":
    x = S.popleft()
    ans = ans - (x * pow(10, len(S), 998244353))
  else:
    print(ans % 998244353)