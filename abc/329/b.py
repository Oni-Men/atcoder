N = int(input())
A = list(map(int, input().split()))

largest = max(A)
second = 0

for a in A:
  if a == largest:
    continue
  if a > second:
    second = a

print(second)
