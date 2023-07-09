from collections import deque


N, M = map(int, input().split())
E = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)


visited = set()

ans = 0

for i in range(1, N+1):
    stack = deque()
    if i in visited:
        continue
    stack.append(i)
    while len(stack) >= 1:
        j = stack.pop()
        if j in visited:
            ans += 1
            continue
        visited.add(j)
        for e in E[j]:
            if e not in visited:
                stack.append(e)

print(ans)
