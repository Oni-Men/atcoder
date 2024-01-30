A = [list(map(int, input().split())) for _ in range(9)]
B = list(range(1, 10))

cond1 = True
cond2 = True
cond3 = True

for y in range(9):
  if sorted(A[y]) != B:
    cond1 = False

for x in range(9):
  if sorted([A[y][x] for y in range(9)]) != B:
    cond2 = False

for i in range(3):
  for j in range(3):
    if sorted([A[i * 3 + y][j * 3 + x] for y in range(3) for x in range(3)]) != B:
      cond3 = False

print("Yes" if cond1 and cond2 and cond3 else "No")