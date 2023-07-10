N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

s = set(C)
if not T in s:
  T = C[0]

ans = 0
value = -1

for i in range(N):
  if C[i] is T and R[i] > value:
    value = R[i]
    ans = i

print(ans+1)