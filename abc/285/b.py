N = int(input())
S = input()

for i in range(1, N):
    k = 0
    while k + i < N and S[k] != S[k+i]:
        k += 1
    print(k)
        