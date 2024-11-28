3. Write a function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Output: 13
