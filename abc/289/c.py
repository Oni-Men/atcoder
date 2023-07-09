N, M = map(int, input().split())
s = []

for _ in range(M):
  input()
  s.append(list(map(int, input().split())))

ans = 0

for b in range(2 ** M):
  t = set()
  for i in range (M):
    if b & (1 << i):
      t |= set(s[i])
  if len(t) == N:
    ans += 1

print(ans)