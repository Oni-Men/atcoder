N, M = map(int, input().split())

E = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)


for i in range(1, N+1):
    E[i].sort()
    print(f"{len(E[i])}", *E[i])
