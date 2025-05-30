from collections import deque

dq = deque()

dq.append(1)         # Right
dq.appendleft(0)     # Left

print(dq)            # deque([0, 1])

dq.pop()             # Remove from right -> 1
dq.popleft()         # Remove from left -> 0

print(dq)            # deque([])
