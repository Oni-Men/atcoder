N = int(input())

yes = 0

for i in range(N):
    if input() == "For":
        yes += 1

print("Yes" if yes > N // 2 else "No")
