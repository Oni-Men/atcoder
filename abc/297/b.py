S = input()

b1 = S.find("B")
b2 = S.find("B", b1+1)

if (b2 - b1) % 2 == 0:
    print("No")
    exit()

k = S.find("K")
r1 = S.find("R")
r2 = S.find("R", r1+1)

if r1 < k < r2:
    print("Yes")
else:
    print("No")
