class UnionTree:
    def __init__(self, vertices) -> None:
        self.tree = {}
        for v in vertices:
            self.tree[v] = None

    def root(self, x) -> int:
        if self.tree[x] == None:
            return x
        return self.root(self.tree[x])

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x, y) -> None:
        x = self.root(x)
        y = self.root(y)
        self.tree[x] = y


N = int(input())
S, T = [""] * N, [""] * N
for i in range(N):
    S[i], T[i] = input().split()

ut = UnionTree(S + T)

for s, t in zip(S, T):
    if ut.is_same(s, t):
        print("No")
        exit()
    ut.unite(s, t)

print("Yes")
