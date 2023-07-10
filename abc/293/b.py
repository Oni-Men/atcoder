N = int(input())
A = list(map(int, input().split()))

yet = set([i+1 for i in range(N)])

for i in range(1, N+1):
  if i in yet:
    yet.discard(A[i-1])

print(len(yet))
for a in yet:
  print(a, end=" ")
print()