N, M = map(int, input().split())
a = list(map(int, input().split()))
ans = []

#連結成分でグループ化
group = []
for i in range(1, N+1):
  group.append(i)
  if len(a) != 0 and i == a[0]:
    a.pop(0)
  else:
    group.reverse()
    ans.append(group)
    group = []

ans.append(group)

for p in ans:
  print(" ".join(map(str, p)), end=" ")

print("")
