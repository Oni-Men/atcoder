from collections import deque


N1, N2, M = map(int, input().split())

E = [[] for _ in range(N1+N2+1)]
visited = set()
for i in range(M):
    x, b = map(int, input().split())
    E[x].append(b)
    E[b].append(x)


def find(n):
    q = deque()
    q.append((n, 0))
    ans = 0
    while q:
        j, d = q.popleft()
        if j in visited:
            continue
        ans = d
        visited.add(j)
        for e in E[j]:
            q.append((e, d+1))
    return ans


d1 = find(1)
d2 = find(N1+N2)

print(d1 + d2 + 1)
