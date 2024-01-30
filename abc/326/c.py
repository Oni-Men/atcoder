N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

left = 0
right = 1

while left < right:
  while right < N and A[right] - A[left] < M:
    right += 1
  ans = max(ans, right - left)
  left += 1

print(ans)