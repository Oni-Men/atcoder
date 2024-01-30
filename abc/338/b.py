S = input()

max_count = 0
count  = [0] * 26

for s in S:
  i = ord(s) - ord('a')
  count[i] += 1
  if count[i] > max_count:
    max_count = count[i]

for i in range(26):
  if count[i] == max_count:
    print(chr(i + ord('a')))
    break