S = list(map(int, input().split()))

ans = True

for i in range(7):
    if S[i] > S[i+1]:
        ans = False

for i in S:
    if not (100 <= i <= 675):
        ans = False
    if i % 25 != 0:
        ans = False

print("Yes" if ans else "No")
