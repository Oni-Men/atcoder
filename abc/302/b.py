h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]


def snuke(i, j, dx, dy):
    a = s[i-2*dy][j-2*dx]
    b = s[i-dy][j-dx]
    c = s[i][j]
    d = s[i+dy][j+dx]
    e = s[i+2*dy][j+2*dx]
    if "".join([a, b, c, d, e]) == "snuke":
        print(i-2*dy + 1, j-2*dx + 1)
        print(i-1*dy + 1, j-1*dx + 1)
        print(i+0*dy + 1, j+0*dx + 1)
        print(i+1*dy + 1, j+1*dx + 1)
        print(i+2*dy + 1, j+2*dx + 1)


for i in range(0, h):
    for j in range(2, w - 2):
        snuke(i, j, 1, 0)
        snuke(i, j, -1, 0)

for i in range(2, h-2):
    for j in range(0, w):
        snuke(i, j, 0, 1)
        snuke(i, j, 0, -1)

for i in range(2, h - 2):
    for j in range(2, w - 2):
        snuke(i, j, 1, 1)
        snuke(i, j, -1, -1)
        snuke(i, j, 1, -1)
        snuke(i, j, -1, 1)
