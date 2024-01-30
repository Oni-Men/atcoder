import math


D = int(input())

ans = D

for x in range(int(D ** 0.5) + 2):
  t = D - x * x
  if t < 0:
    # y = 0が最適
    ans = min(ans, abs(t))
  else:
    y1 = math.ceil(t ** 0.5)
    y2 = math.floor(t ** 0.5)
    ans = min(ans, abs(y1**2 - t), abs(y2**2 - t))

print(ans)