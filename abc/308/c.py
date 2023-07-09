class Toss(object):
    def __init__(self, id, a, b):
        self.id = id
        self.a = a
        self.b = b

    def __lt__(self, other):
        x = self.a * (other.a + other.b)
        y = other.a * (self.a + self.b)
        if x == y:
            return self.id > other.id
        return x < y


N = int(input())
P = [0] * N

for i in range(N):
    a, b = map(int, input().split())
    P[i] = Toss(i+1, a, b)

P = sorted(P, reverse=True)
print(*map(lambda x: x.id, P))
