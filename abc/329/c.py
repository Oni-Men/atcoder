N = int(input())
S = list(input())

alphabets = [0]  * 26

left = 0
right = 1
while left < right and left < N:
  while right < N and S[left] == S[right]:
    right += 1
  k = ord(S[left]) - ord('a')
  alphabets[k] = max(alphabets[k], right - left)
  left = right
  right = left + 1
  
print(sum(alphabets))
