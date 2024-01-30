N = int(input())
D = list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
  for j in range(1, D[i-1]+1):
    s = str(i) + str(j)
    zoro = True
    for t in s:
      if t != s[0]:
        zoro = False
        break
    
    if zoro:
      ans += 1

print(ans)