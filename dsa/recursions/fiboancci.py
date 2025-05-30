def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(fibonacci(i), end=' ')  # 0 1 1 2 3 5 8
