S = input()

i = 0
while i < len(S):
  if S[i:i+3] == "ABC":
    S = S[:i] + S[i+3:]
    i -= 3
  else:
    i += 1
  if i < 0:
    i = 0

print(S)