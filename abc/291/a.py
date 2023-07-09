S = input()

ans = -1

for i in range(len(S)):
    if S[i].isupper():
        ans = i + 1
        break

print(ans)
