N = int(input())
A = list(map(int, input().split()))

ans = True

for i in range(N - 1):
    if A[i] != A[i + 1]:
        ans = False

if A[N-1] != A[0]:
    ans = False

print("Yes" if ans else "No")
