N = int(input())

d = [0] * (N+1)
d[0] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if i * j >= N+1:
            break
        d[i * j] += 1

ans = 0

for ab in range(1, N+1):
    cd = N - ab
    ans += d[ab] * d[cd]

print(ans)
