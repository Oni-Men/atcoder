N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for a in range(10**6+1):
  end = False
  for i in range(N):
    if Q[i] - A[i] * a < 0:
      end = True
  if end:
    break

  b = 10**6
  for i in range(N):
    if B[i] != 0:
      b = min(b, (Q[i] - a * A[i]) // B[i])

  ans = max(ans, a + b)

print(ans)