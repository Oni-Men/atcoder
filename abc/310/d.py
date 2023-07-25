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


N, T, M = map(int, input().split())
A = [0] * M
B = [0] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())

teams = [set() for _ in range(T)]
