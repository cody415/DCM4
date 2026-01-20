import math

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calculate HCF/GCD
hcf = math.gcd(a, b)

print(f"The HCF/GCD of {a} and {b} is {hcf}")
