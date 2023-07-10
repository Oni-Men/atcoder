H, W = map(int, input().split())

for i in range(H):
  s = list(map(int, input().split()))
  for j in range(W):
    if s[j] == 0:
      print(".", end="")
    else:
      print(chr(s[j]+64), end="")
  print("")