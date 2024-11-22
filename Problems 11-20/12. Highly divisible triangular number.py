import numpy as np
import time as time

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    else:
        i = 5
        while i*i <= n:
            if n%i == 0 or n%(i+2) == 0:
                return False
            i += 6
        return True
    
def prime_factorization(n):
    prime_factors = []
    i = 2
    while n > 1:
        if is_prime(i):
            while n%i == 0:
                prime_factors.append(i)
                n /= i
        i += 1
    return prime_factors

def num_divisors(n):
    prime_factors = prime_factorization(n)
    prime_factors = dict((i, prime_factors.count(i)) for i in prime_factors)

    result = 1
    for i in prime_factors.values():
        result *= (i+1)
    return result

start = time.time()
    
triangle = 1
i = 1
while num_divisors(triangle) < 500:
    i += 1
    triangle += i

print(triangle)
end = time.time()
print(end - start)