import time as time

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n%2 == 0 or n%3 == 0:
        return False
    else:
        for i in range(5, int(n**(1/2))+1, 6):
            if n%i == 0 or n%(i+2) == 0:
                return False
                break
        return True

tic = time.time()

primes = []
cond = True
result = []

n = 1

while cond:
    if is_prime(n):
        primes.append(n)
        i = 0
        while i < len(primes):
            sum_primes = sum(primes[i:])
            if (is_prime(sum_primes)) and (len(primes[i:]) > len(result)):
                if sum_primes < 10**6:
                    result = primes[i:]
                else:
                    cond = False
                    break
            i += 1           
    n += 1

toc = time.time()

print(sum(result))
print(toc-tic)