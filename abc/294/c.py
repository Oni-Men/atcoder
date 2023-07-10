N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
C.sort()

def find(n, arr):
  ok = len(arr)
  ng = -1
  while abs(ok - ng) > 1:
    mid = int((ok + ng) / 2)
    if n < arr[mid]:
      ok = mid
    else:
      ng = mid
  return ok

for a in A:
  print(find(a, C), end=" ")

print()

for b in B:
  print(find(b, C), end=" ")

print()