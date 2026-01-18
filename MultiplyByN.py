# Function 1: Direct multiplication (single iteration)
def multiply_direct(n, m):
    return n * m

# Function 2: Repeated addition (N iterations)
def multiply_iterative(n, m):
    result = 0
    for _ in range(n):   # loop runs N times
        result += m
    return result

# Driver code
N = int(input("Enter value of N: "))
M = int(input("Enter value of M: "))

print("\nUsing direct multiplication:")
print(f"{N} x {M} = {multiply_direct(N, M)}")

print("\nUsing repeated addition (N iterations):")
print(f"{N} x {M} = {multiply_iterative(N, M)}")
