def dfs(tile, x, y, w, h):
    if tile[y][x] == "@":
        return 0
    if tile[y][x] == "#":
        return 0
    tile[y][x] = '@'  # mark
    ans = 1
    if x + 1 < w:
        ans += dfs(tile, x + 1, y, w, h)
    if x - 1 >= 0:
        ans += dfs(tile, x - 1, y, w, h)
    if y - 1 >= 0:
        ans += dfs(tile, x, y - 1, w, h)
    if y + 1 < h:
        ans += dfs(tile, x, y + 1, w, h)
    return ans


def solve():
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        return False
    tile = [list(input()) for _ in range(h)]
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if tile[i][j] == "@":
                x, y = j, i

    tile[y][x] = "."
    ans = dfs(tile, x, y, w, h)
    print(ans)
    return True


while solve():
    pass
