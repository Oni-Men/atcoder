N = int(input())
D = [None] * N

for i in range(N):
  D[i] = [*map(int, input().split())]

D.sort(key=lambda d: d[1], reverse=True)

ans = []

def satisfication(i, j):
  s1 =  max(D[i][1], D[j][1])
  s2 =  min(D[i][1], D[j][1])
  if D[i][0] == D[j][0]:
    return s1 + s2 // 2
  else:
    return s1 + s2


i = 0
j = 1
while j < len(D) - 1:
  if D[i][0] != D[j][0]:
    break
  j += 1

ans1 = satisfication(0, 1)
ans2 = satisfication(i, j)

print(max(ans1, ans2))