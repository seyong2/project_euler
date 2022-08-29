import time as time

# define a function that determines whether a number is prime or not
def is_prime(n):
    if n in [0, 1]:
        return False
    elif n in [2, 3]:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
                break
            else:
                continue
        return True

# define a function that gives a list of unique prime factors of a number
def prime_factorization(n):
    factors = []
    if is_prime(n):
        factors.append(n)
    else:
        i = 2
        while n != 1:
            if n%i == 0:
                n /= i
                factors.append(i)
            else:
                i += 1
    return list(set(factors))

# define a function that determines whether two numbers are relatively primes or not
def relatively_primes(n, m):
    factors_n = prime_factorization(n)
    factors_m = prime_factorization(m)
    if any(i in factors_m for i in factors_n):
        return False
    else:
        return True

# define Euler's Totient function, φ(n), that gives the number of numbers less than n which are relatively prime to n
def phi(n):
    prime_factors = prime_factorization(n)
    phi = n
    if len(prime_factors)==1:
        phi -= n/prime_factors[0]
    else:
        for i in prime_factors:
            phi *= (1 - 1/i)
    return phi

tic = time.time()

n_phi = {} # empty dictionary

n = 2 # starts from 2

while True:
    if n not in n_phi.keys(): # check whether n is in n_phi.keys()
        phi_n = phi(n)
        n_phi[n] = n/phi_n
        
        # Euler's Totient function is a multiplicative function. 
        # Then, if two numbers, m and n, are relatively primes, φ(m*n) = φ(m)*φ(n).
        # First, we obtain a list of primes relative to n.
        relatively_primes_list = [i for i in range(2, n) if relatively_primes(i, n)]
        
        # Next, if i*n is not in n_phi.keys(), we compute φ(i)*φ(n).
        for i in relatively_primes_list:
            if i*n not in n_phi.keys():
                n_phi[i*n] = (i*n)/(phi_n*phi(i))
    
    # We stop when the maximum key is greater than 10**6
    if max(n_phi.keys()) > 10**6:
        break
    else:
        n += 1

toc = time.time()

print(max(n_phi, key=n_phi.get))
print(toc - tic)