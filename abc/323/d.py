from collections import defaultdict
import heapq

N = int(input())
S = []
C = defaultdict(lambda: 0)


for i in range(N):
    s,  c = map(int, input().split())
    S.append(s)
    C[s] = c

heapq.heapify(S)

ans = 0

while S:
    s = heapq.heappop(S)
    c = C[s]
    if c % 2 == 1:
        ans += 1
    s = 2 * s
    c = c // 2
    if c == 0:
        continue
    if s not in C:
        heapq.heappush(S, s)
        C[s] = c
    else:
        C[s] += c

print(ans)
