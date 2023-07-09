S = [list(input()) for _ in range(8)]

T = "abcdefgh"

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            print(T[j]+str(8-i))
