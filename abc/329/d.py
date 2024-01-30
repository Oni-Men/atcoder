N, M = map(int, input().split())
A = list(map(int, input().split()))

votes = [0] * N
current = 0

for a in A:
  a -= 1
  votes[a] += 1
  if votes[a] > votes[current]:
    current = a
  if votes[a] == votes[current]:
    current = min(current, a)
  print(current+1)