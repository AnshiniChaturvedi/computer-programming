6. Write a function to calculate the power of a number.
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))  # Output: 8
