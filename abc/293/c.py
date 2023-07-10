from collections import deque

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def test(x, y, passed):
  if x >= W or y >= H:
    return 0
  num = A[y][x]

  if num in passed:
    return 0
  
  if x + 1 == W and y + 1 == H:
    return 1
  
  passed = passed.copy()
  passed.add(num)

  return test(x + 1, y, passed) + test(x, y + 1, passed)

ans = test(0, 0, set())
print(ans)