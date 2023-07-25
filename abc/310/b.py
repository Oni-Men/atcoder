N, M = map(int, input().split())
P, C, F = [0] * N, [0] * N, [None] * N
for i in range(N):
    P[i], C[i], *F[i] = map(int, input().split())
    F[i] = set(F[i])

ans = False

for i in range(N):
    for j in range(N):
        if P[i] >= P[j]:
            if F[j] >= F[i]:
                if P[i] > P[j] or len(F[j] - F[i]) > 0:
                    ans = True


print("Yes" if ans else "No")
