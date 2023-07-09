from collections import deque

N = int(input())
S = input()

stack = deque()

i = 0
while i < len(S):
    if S[i] == "(":
        stack.append(i)
    if S[i] == ")":
        if len(stack) >= 1:
            j = stack.pop()
            S = S[:j] + S[i+1:]
            i = j - 1
    i += 1

print(S)
