from collections import deque

# (abc(def)(def)(hij)xyz)
# (abc(def)(def)(abc)xyz)
# (abc)def(abc)
# abc(def)(abc)(def)

S = input()
B = {}

ok = True
W = deque()
W.append(set())

for i, s in enumerate(S):
	if s == '(':
		W.append(set())
	elif s == ')':
		w = W.pop()
		for k in w:
			B[k] = False
		if len(W) != 0:
			W[-1].union(w)
	else:
		if s in B and B[s]:
			ok = False
			break
		B[s] = True
		W[-1].add(s)
		

print("Yes" if ok else "No")