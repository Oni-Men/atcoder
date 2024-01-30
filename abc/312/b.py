N, M = map(int, input().split())
S = [input() for _ in range(N)]


ans = [[False] * M for _ in range(N)]

for i in range(N-8):
    for j in range(M-8):
        flg = True
        flg &= S[i][j:j+4] == "###."
        flg &= S[i+1][j:j+4] == "###."
        flg &= S[i+2][j:j+4] == "###."
        flg &= S[i+3][j:j+4] == "...."

        flg &= S[i+5][j+5:j+9] == "...."
        flg &= S[i+6][j+5:j+9] == ".###"
        flg &= S[i+7][j+5:j+9] == ".###"
        flg &= S[i+8][j+5:j+9] == ".###"
        if flg:
            ans[i][j] = True

for i in range(N):
    for j in range(M):
        if ans[i][j]:
            print(i+1, j+1)
