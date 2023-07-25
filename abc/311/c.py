from collections import deque


N = int(input())
A = [i - 1 for i in list(map(int, input().split()))]

visited = set()
q = deque()
q.append(0)

while q:
    j = q.popleft()
    if j in visited:
        break
    visited.add(j)
    q.append(A[j])

ans = []
start = j
while True:
    ans.append(j+1)
    j = A[j]
    if j == start:
        break

print(len(ans))
print(*ans)
