N, M = map(int, input().split())
A = list(map(int, input().split()))

P = [i + 1 for i in range(N)]
Q = [None] * N

for i in range(N):
    S = input()
    Q[i] = [*A]
    for j in range(M):
        if S[j] == 'o':
            P[i] += A[j]
            Q[i][j] = 0

top = max(P)

for i in range(N):
    Q[i].sort(reverse=True)
    pi = P[i]
    j = 0
    while pi < top:
        pi += Q[i][j]
        j += 1
    print(j)
