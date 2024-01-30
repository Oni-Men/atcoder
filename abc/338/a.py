S = input()

capitalized = True

if S[0].islower():
  capitalized = False

for s in S[1:]:
  if s.isupper():
    capitalized = False

print("Yes" if capitalized else "No")