N = int(input())
H = list(map(int, input().split()))

ans = 0
longest = H[0]

for i in range(N):
    if H[i] > longest:
        longest = H[i]
        ans = i

print(ans+1)
