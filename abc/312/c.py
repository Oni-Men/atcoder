N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = B[0]+1

i = 0
j = 0

while True:
    if A[i] <= B[j]:
        if i >= j:
            ans = A[i]
    else:
        break
    if i + 1 < N:
        i += 1
    if j + 1 < M:
        j += 1
    if i + 1 == N and j + 1 == M:
        break

print(ans)
