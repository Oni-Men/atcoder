S = [input() for i in range(9)]

X = []
Y = []

for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            X.append(j)
            Y.append(i)

ans = set()


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


for p1 in zip(X, Y):
    for p2 in zip(X, Y):
        d1 = distance(p1, p2)
        if d1 == 0:
            continue
        for p3 in zip(X, Y):
            d2 = distance(p2, p3)
            if d2 == 0 or distance(p1, p3) == 0:
                continue
            for p4 in zip(X, Y):
                d3 = distance(p3, p4)
                d4 = distance(p4, p1)
                if d3 == 0 or d4 == 0 or distance(p4, p2) == 0:
                    continue
                if d1 == d2 == d3 == d4:
                    if distance(p1, p3) == distance(p2, p4):
                        sq = [p1, p2, p3, p4]
                        sq = sorted(sq, key=lambda x: (x[0], x[1]))
                        ans.add(tuple(sq))

print(len(ans))
