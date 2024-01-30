# respect https://atcoder.jp/contests/abc337/submissions/49455875
# https://imoz.jp/algorithms/imos_method.html

H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = K + 1

if K <= W:
  for y in range(H):
    dot = S[y][:K].count(".")
    bad = S[y][:K].count("x")
    if bad == 0:
      ans = min(ans, dot)

    for j in range(K, W):
      if S[y][j] == ".":
        dot += 1
      elif S[y][j] == "x":
        bad += 1

      if S[y][j-K] == ".":
        dot -= 1
      elif S[y][j-K] == "x":
        bad -= 1
        
      if bad == 0:
        ans = min(ans, dot)


if K <= H:
  for x in range(W):
    dot = [S[i][x] for i in range(K)].count(".")
    bad = [S[i][x] for i in range(K)].count("x")
    if bad == 0:
      ans = min(ans, dot)

    for i in range(K, H):
      if S[i][x] == ".":
        dot += 1
      elif S[i][x] == "x":
        bad += 1
      
      if S[i-K][x] == ".":
        dot -= 1
      elif S[i-K][x] == "x":
        bad -= 1
    
      if bad == 0:
        ans = min(ans, dot)

print(-1 if ans > K else ans)