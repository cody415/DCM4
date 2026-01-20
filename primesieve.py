def sieve_of_eratosthenes(n):
    # Step 1: Initialize a boolean array
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False  # 0 and 1 are not prime
    
    p = 2
    while p * p <= n:
        if prime[p]:
            # Step 2: Mark multiples of p as False
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    # Step 3: Collect all prime numbers
    primes = [i for i in range(n+1) if prime[i]]
    return primes

# Example usage
num = int(input("Find primes up to: "))
print(f"Prime numbers up to {num} are: {sieve_of_eratosthenes(num)}")
