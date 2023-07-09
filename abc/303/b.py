n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

pair = set()


for line in a:
    for i in range(1, len(line)):
        x = line[i-1]
        y = line[i]
        if y < x:
            x, y = y, x
        pair.add((x, y))

print((n) * (n - 1) // 2 - len(pair))
