R, C = map(int, input().split())
B = [[0] * C for _ in range(R)]

for r in range(R):
  row = input()
  for c in range(C):
    if row[c] is "#":
      B[r][c] = -1
    elif row[c] is not ".":
      B[r][c] = int(row[c])

for r in range(R):
  for c in range(C):
    if B[r][c] <= 0:
      continue
    p = B[r][c]
    B[r][c] = 0
    for y in range(r-p, r+p+1):
      for x in range(c-p, c+p+1):
        if (abs(x-c) + abs(y-r)) > p:
          continue
        if (y >= 0 and y < R) and (x >= 0 and x < C):
          if B[y][x] is -1:
            B[y][x] = 0

for r in range(R):
  for c in range(C):
    print("#" if B[r][c] is -1 else ".", end="")
  print("")