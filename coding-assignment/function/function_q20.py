20. Write a function to convert a decimal number to binary.
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

print(decimal_to_binary(10))  # Output: "1010"
