N = int(input())
S = input()

if N == 1:
    print(1)

R = 0
G = 0
B = 0

for s in S:
    if s == "R":
        R += 1
    if s == "G":
        G += 1
    if s == "B":
        B += 1

ans = R * G * B


for x in range(1, N):
    for i in range(N):
        j = i + x
        k = i + 2*x
        if k >= N:
            break
        if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            ans -= 1

print(ans)
