import bisect


N, M , P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

C = [0] * (M + 1)
C[1] = B[0]
for i in range(1, M):
  C[i + 1] = C[i] + B[i]

ans = 0

for a in A:
  i = bisect.bisect_right(B, P - a)
  ans += C[i] + a * i
  ans += P * (M - i)


print(ans)