M = int(input())
S = [input() for _ in range(3)]

T = [sorted(list(s)) for s in S]

if T[0] != T[1] or T[1] != T[2] or T[2] != T[0]:
  print(-1)
  exit()

ans = 0

for i in S[0]:
  

print(ans)