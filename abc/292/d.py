from collections import deque


N, M = map(int, input().split())

E = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

visited = set()
stack = deque()

ans = True

for i in range(1, N+1):
    vertices = 0
    edges = 0
    loops = 0
    stack.append(i)
    while len(stack) >= 1:
        j = stack.pop()
        if j in visited:
            continue
        visited.add(j)
        vertices += 1
        for e in E[j]:
            stack.append(e)
            if j == e:
                loops += 1
            else:
                edges += 1
    if vertices != edges // 2 + loops // 2:
        ans = False

print("Yes" if ans else "No")
