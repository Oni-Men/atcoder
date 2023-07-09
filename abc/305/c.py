h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

top = h + 1
left = w + 1
bot = - 1
right = -1

for y in range(h):
    for x in range(w):
        if grid[y][x] != "#":
            continue
        top = min(top, y)
        bot = max(bot, y)
        left = min(left, x)
        right = max(right, x)

ans_x, ans_y = -1, -1
for y in range(top, bot + 1):
    for x in range(left, right + 1):
        if grid[y][x] == ".":
            ans_x = x
            ans_y = y

print(ans_y+1, ans_x+1)
