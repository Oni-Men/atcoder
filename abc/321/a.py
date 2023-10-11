N = input()

ans = True

for i in range(len(N) - 1):
  m = N[i]
  n = N[i + 1]
  if m <= n:
    ans = False

print("Yes" if ans else "No")