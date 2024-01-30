N, M = map(int, input().split())
A = list(map(int, input().split()))

j = 0

for i in range(1,N+1):
  next_party = A[j]
  print(next_party - i)
  if next_party == i:
    j += 1