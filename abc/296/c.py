N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = False
r = 0
for l in range(N):
    while r < N and A[r] - A[l] <= X:
        if A[r] - A[l] == X:
            ans = True
        r += 1

print("Yes" if ans else "No")
