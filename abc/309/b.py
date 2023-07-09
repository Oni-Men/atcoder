N = int(input())
A = [list(input()) for _ in range(N)]

B = [A[i][:] for i in range(N)]

for i in range(N-1):
    B[i][0] = A[i+1][0]
    B[i+1][-1] = A[i][-1]

B[0] = [A[1][0]] + A[0][:-1]
B[-1] = A[-1][1:] + [A[-2][-1]]

for b in B:
    print("".join(b))
