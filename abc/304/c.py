import sys
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
x, y = [0] * n, [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

neighbors = {}
for i in range(n):
    neighbors[i] = set()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= d ** 2:
            neighbors[i].add(j)
            neighbors[j].add(i)

infected = set()


def dfs(i):
    if i in infected:
        return
    infected.add(i)
    for j in neighbors[i]:
        dfs(j)


dfs(0)

for i in range(n):
    print("Yes" if i in infected else "No")
