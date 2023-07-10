N = int(input())
W = input().split()

correct = ["and", "not", "that", "the", "you"]

ans = False

for w in W:
  if w in correct:
    ans = True
    break

print("Yes" if ans else "No")