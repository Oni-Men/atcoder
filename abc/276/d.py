N = int(input())
A = list(map(int, input().split()))

m = min(A)

has2x = False
has3x = False

i = 0
while True:
    m = min(A)
    for i in range(N):
        if m == A[i]:
            continue
        if A[i] % 2 == 0:
            has2x = True

        if A[i] % 3 == 0:
            has3x = True

    if not has2x and not has3x:
        break
