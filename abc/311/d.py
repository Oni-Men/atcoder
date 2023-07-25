from collections import deque


N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

seen = set()
q = deque()
q.append((1, 1))

while q:
    i, j = q.popleft()
    if (i, j) in seen:
        continue
    seen.add((i, j))
    for di, dj in D:
        k, l = i, j
        while S[k + di][l + dj] == ".":
            seen.add((k, l))
            k += di
            l += dj
        if (k, l) not in seen:
            q.append((k, l))

print(len(seen))
