import time
Ha, Wa = map(int, input().split())
A = [list(input()) for _ in range(Ha)]

Hb, Wb = map(int, input().split())
B = [list(input()) for _ in range(Hb)]

Hx, Wx = map(int, input().split())
X = [list(input()) for _ in range(Hx)]

ans = False

for ay in range(-Ha-1, Ha+2):
    for ax in range(-Wa-1, Wa+2):
        for by in range(-Hb-1, Hb+2):
            for bx in range(-Wb-1, Wb+2):
                flg = True
                for i in range(Hx):
                    for j in range(Wx):
                        if 0 <= ay + i < Ha and 0 <= ax + j < Wa:
                            a = A[ay + i][ax + j]
                        else:
                            a = "."

                        if 0 <= by + i < Hb and 0 <= bx + j < Wb:
                            b = B[by + i][bx + j]
                        else:
                            b = "."
                        tile = "#" if (a == "#" or b == "#") else "."
                        if X[i][j] != tile:
                            flg = False

                ans |= flg

print("Yes" if ans else "No")
