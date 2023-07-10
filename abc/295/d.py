S = input()
N = len(S)

# 20230322

# 数えたいもの：　条件を満たさない区間
# 答えたい値：　条件を満たす区間の数

ans = 0
right = 0
cond = set()
for left in range(N):
  while right < N:
    c = S[right]
    if c in cond:
      cond.remove(c)
    else:
      cond.add(c)
    right += 1
    if len(cond) == 0:
      break
  
  ans += right - left

  if left == right:
    right += 1
  cond.discard(S[left])

print(int(N * (N + 1) / 2) - ans)