N = int(input())
S = input()

bars = 0

ans = False

for s in S:
  if s is "|":
    bars += 1
  if s is "*" and bars == 1:
    ans = True
    break

print("in" if ans else "out")