from collections import deque


H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = "snuke"

visited = set()
stack = deque()
stack.append((0, (0, 0)))

ans = False

while len(stack) >= 1:
    i, pos = stack.pop()
    if S[pos[1]][pos[0]] != T[i]:
        continue
    if pos in visited:
        continue
    visited.add(pos)

    if pos[0] == W-1 and pos[1] == H-1:
        ans = True
        break

    for dx, dy in d:
        nx = pos[0] + dx
        ny = pos[1] + dy
        if 0 <= nx < W and 0 <= ny < H:
            stack.append(((i+1) % 5, (nx, ny)))


print("Yes" if ans else "No")
