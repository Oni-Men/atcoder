H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for j in range(H):
    for i in range(W-1):
        if S[j][i] == "T" and S[j][i+1] == "T":
            S[j][i] = "P"
            S[j][i+1] = "C"


for s in S:
    print("".join(s))
