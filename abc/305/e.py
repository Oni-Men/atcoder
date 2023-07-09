N, M, K = map(int, input().split())
A, B = [0] * N, [0] * N
P, K = [0] * M, [0] * M

for i in range(N):
    A[i], B[i] = map(int, input().split())

for i in range(M):
    P[i], K[i] = map(int, input().split())
