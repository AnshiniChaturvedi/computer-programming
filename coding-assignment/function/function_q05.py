5. Write a function to find the greatest common divisor (GCD) of two numbers.
python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # Output: 6
