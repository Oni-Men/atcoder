from collections import defaultdict, deque


N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = True
E = defaultdict(lambda: set())
V = [-1] * (N+1)

for a, b in zip(A, B):
  E[a].add(b)
  E[b].add(a)

q = deque([(i, 0) for i in range(1, N+1)])
stop = False
while q and not stop:
  i, color  = q.popleft()
  if V[i] != -1:
    continue

  V[i] = color

  for j in E[i]:
    if V[j] == -1:
      q.appendleft((j, 1 - color))
    elif V[j] == color:
      ans = False
      stop = True

print("Yes" if ans else "No")