N = int(input())
S = input()

prev = ""
ans = True

for s in S:
  if prev == "":
    prev = s
    continue
  if prev == s:
    ans = False
    break
  prev = s

print("Yes") if ans else print("No")