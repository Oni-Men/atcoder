N = int(input())
Q = int(input())

cards = {} 
boxes =  {} 

for _ in range(Q):
  line = input().split()
  q = line[0]
  i = int(line[1])
  if q is "1":
    j = int(line[2])
    if j not in cards:
      cards[j] = []
    if i not in boxes:
      boxes[i] = set()
    cards[j].append(i)
    boxes[i].add(j)
  elif q is "2":
    print(" ".join(map(str, sorted(cards[i]))))
  else:
    print(" ".join(map(str, sorted(boxes[i]))))