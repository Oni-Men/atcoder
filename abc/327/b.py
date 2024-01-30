B = int(input())

ans = -1

a = 1
while True:
  t = a ** a
  if t > B:
    break
  if t == B:
    ans = a
    break
  a += 1

print(ans)