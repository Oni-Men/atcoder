N, M = map(int, input().split())

V = [set() for _ in range(N)]

for i in range(M):
	u, v = map(int, input().split())
	u -= 1
	v -= 1
	V[u].add(v)
	V[v].add(u)

ans = 0

Fixed = {}
for i in range(N):
	Fixed[i] = False

def explore(i, cid):
	global V, Fixed, Cs, N, M
	if Fixed[i]:
		return False
	Fixed[i] = True
	children = V[i]
	for child in children:
		explore(child, cid)
	return True

for i in range(N):
	if explore(i, i):
		ans += 1

print(ans)
