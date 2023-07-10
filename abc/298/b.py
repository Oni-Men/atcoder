N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

ans = False

def check():
  for y in range(N):
    for x in range(N):
      if A[y][x] == 1:
        if B[y][x] != 1:
          return False
  return True

for _ in range(4):
  C = [[0] * N for _ in range(N)]
  for y in range(N):
    for x in range(N):
      C[y][x] = A[N-x-1][y]
  A = C
  if check():
    ans = True
    break

print("Yes" if ans else "No")