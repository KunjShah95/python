from collections import deque

stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

# Pop
print(stack.pop())  # 30
print(stack[-1])    # Peek -> 20
print(stack)        # [10, 20]


#✅ .append() to push, .pop() to pop (from end)


stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())  # 30
print(stack[-1])    # 20
print(stack)        # deque([10, 20])
