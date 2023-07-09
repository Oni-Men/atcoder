from collections import deque

N = int(input())
A = {}
B = {}

for i in range(N):
    a, b = map(int, input().split())
    if a not in A:
        A[a] = []
    if b not in B:
        B[b] = []
    A[a].append(b)
    B[b].append(a)

ans = 1

q = deque()
visited = set()
q.append(1)
while len(q) != 0:
    pop = q.pop()
    if pop in visited:
        continue
    visited.add(pop)
    ans = max(ans, pop)
    if pop in A:
        for to in A[pop]:
            q.append(to)
    if pop in B:
        for to in B[pop]:
            q.append(to)

print(ans)
