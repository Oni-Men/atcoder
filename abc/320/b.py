S = input()
L = len(S)

ans = 0

def is_palindrome(s):
  if len(s) < 2:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])

for i in range(L):
  for j in range(i, L+1):
    s = S[i:j]
    if is_palindrome(s):
      ans = max(ans, j - i)

print(ans)