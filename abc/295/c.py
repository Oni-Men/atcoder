N = int(input())
A = list(map(int, input().split()))

fragments = set()
ans = 0

for a in A:
  if a in fragments:
    fragments.remove(a)
    ans+=1
  else:
      fragments.add(a)

print(ans)