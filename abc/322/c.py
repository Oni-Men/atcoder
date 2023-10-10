K = int(input())

A = []

for i in range(1, 2 ** 10):
  n = 0
  for j in range(10):
    if (i >> j) & 1:
      n *= 10
      n += 9 - j
  
  A.append(n)

A.sort()
print(A[K])