from collections import deque


N, M = map(int, input().split())
E = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

ep = 0

for i in range(1, N+1):
    degree = len(E[i])
    if degree > 2:
        print("No")
        exit()
    if degree == 1:
        ep += 1

if ep != 2:
    print("No")
    exit()

stack = deque()
visited = set()

stack.append(1)
while len(stack) >= 1:
    j = stack.pop()
    if j in visited:
        continue
    visited.add(j)
    for e in E[j]:
        stack.append(e)

for i in range(1, N+1):
    if i not in visited:
        print("No")
        exit()

print("Yes")
