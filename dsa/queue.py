from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())  # 1
print(queue)            # deque([2, 3])

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))  # 1
print(queue)         # [2, 3]

# ❌ .pop(0) is slow for large queues (O(n) time)

