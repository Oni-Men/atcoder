N, Q = map(int, input().split())

P = [0] * N

for i in range(Q):
    q, x = map(int, input().split())
    x -= 1
    if q == 1:
        P[x] += 1
    elif q == 2:
        P[x] = 2
    else:
        print("Yes" if P[x] == 2 else "No")
