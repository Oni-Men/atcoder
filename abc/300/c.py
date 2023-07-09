h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = [0] * min(h, w)
dx = [1, -1, 1, -1]
dy = [1, -1, -1, 1]


def check(n, i, j):
    if c[i][j] != "#":
        return False
    ok = True
    tiles = []
    for k in range(1, n+1):
        for x, y in zip(dx, dy):
            tx = j + k * x
            ty = i + k * y
            tiles.append((ty, tx))
            if c[ty][tx] != "#":
                ok = False
    if ok:
        for tile in tiles:
            c[tile[0]][tile[1]] = "."
    return ok


for n in range(min(h, w), 0, -1):
    for i in range(n, h-n):
        for j in range(n, w-n):
            if check(n, i, j):
                ans[n-1] += 1


print(*ans)
