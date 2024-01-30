N, M = map(int, input().split())
T = input()
S = input()

if S.startswith(T) and S.endswith(T):
  print(0)
else:
  if S.startswith(T):
    print(1)
  elif S.endswith(T):
    print(2)
  else:
    print(3)