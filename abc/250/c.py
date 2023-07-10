N, Q = map(int, input().split())
A = [i for i in range(1, N+1)]

for i in range(Q):
  x = int(input())
  x -= 1
  if x == N - 1:
    A[0], A[x] = A[x], A[0]
  else:
    A[x], A[x+1] = A[x+1], A[x]
  print(A)
print(" ".join(map(str, A)))