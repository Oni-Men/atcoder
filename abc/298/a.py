N = int(input())
S = input()

ok = False
ng = False

for s in S:
  if s == 'o':
    ok = True
  if s == 'x':
    ng = True
    break

print("Yes" if (ok and not ng) else "No")