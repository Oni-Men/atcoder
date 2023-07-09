N, K = map(int, input().split())
A = set(map(int, input().split()))
A = list(A)
A.sort()

ans = 0
for i in range(0, min(K, len(A))):
  if A[i] != i: break
  ans = i + 1

print(ans)