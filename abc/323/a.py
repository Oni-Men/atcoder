S = input()

ans = True
for i in range(1, len(S), 2):
    if S[i] == '1':
        ans = False

print("Yes" if ans else "No")
