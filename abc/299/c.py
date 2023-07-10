N = int(input())
S = input()

ans = -1

O = list(filter(lambda x: x > 0, map(lambda x: len(x), S.split("-"))))
if len(O) > 1:
  ans = max(O)
elif len(O) == 1 and (S[0] is "-" or S[-1] is "-"):
  ans = max(O)

print(ans)