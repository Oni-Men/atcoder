from collections import deque

N = 100
E = [[] for _ in range(N)]

for _ in range(N):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

q = deque()
visited = [False] * N

while q:
    i = q.popleft()
    if visited[i]:
        continue
    visited[i] = True
    for j in E[i]:
        q.append(j)
