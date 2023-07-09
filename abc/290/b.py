N, K = map(int, input().split())
S = input()

cnt = 0
for i in S:
  if cnt < K:
    print(i, end="")
  else:
    print("x", end="")
  if i == "o": cnt+= 1

print()